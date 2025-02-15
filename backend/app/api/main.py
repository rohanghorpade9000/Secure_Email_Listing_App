from fastapi import FastAPI
from backend.app.api.endpoints.auth import router as auth_router
from backend.app.api.endpoints.emails import router as emails_router

app = FastAPI()

app.include_router(emails_router)
app.include_router(auth_router, prefix="/auth")
