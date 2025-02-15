from fastapi import APIRouter, HTTPException, Depends
from backend.app.api.db.mongodb import users_collection
from backend.app.api.endpoints.security.hashing import hash_password, verify_password
from backend.app.api.endpoints.security.jwt_auth import create_access_token
from pydantic import BaseModel

router = APIRouter()

# Request Models
class UserSignup(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

# Signup
@router.post("/signup")
async def signup(user: UserSignup):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Store password in plaintext (No hashing for now)
    await users_collection.insert_one({
        "email": user.email,
        "password": user.password  # Plaintext password
    })

    return {"message": "User registered successfully"}

# Login
@router.post("/login")
async def login(user: UserLogin):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or user.password != db_user["password"]:  # Direct comparison (no hashing)
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT Token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


