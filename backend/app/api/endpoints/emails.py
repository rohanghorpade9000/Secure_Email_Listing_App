from fastapi import APIRouter, Depends, HTTPException
from backend.app.services.email_service import fetch_emails
from backend.app.api.endpoints.security.jwt_auth import verify_jwt_token
import os
from fastapi.responses import FileResponse

router = APIRouter()

# Fetch emails (Uses logged-in user's email)
@router.get("/emails")
async def get_emails(user_email: str = Depends(verify_jwt_token)):
    emails = await fetch_emails(user_email)  # Use await here
    if "error" in emails:
        raise HTTPException(status_code=400, detail=emails["error"])
    return {"emails": emails}

# Download an attachment (Also requires authentication)
@router.get("/emails/{filename}/download")
async def download_attachment(filename: str, user_email: str = Depends(verify_jwt_token)):
    file_path = f"backend/attachments/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=filename)
