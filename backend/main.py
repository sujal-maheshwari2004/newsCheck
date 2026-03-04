from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from agent import process_youtube_link
import os
import json
import re

# CORS IMPORT
from fastapi.middleware.cors import CORSMiddleware

# AUTH IMPORTS
from auth.router import router as auth_router
from auth.dependencies import get_current_user
from auth.utils import check_usage_allowed, record_usage


app = FastAPI()

# REGISTER AUTH ROUTES
app.include_router(auth_router, prefix="/auth")

# CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://newscheck-frontend.onrender.com",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Regex pattern to validate YouTube URLs
YOUTUBE_URL_PATTERN = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')


class YouTubeLink(BaseModel):
    youtube_link: str


@app.post("/process/")
async def process_youtube(
    youtube_link: YouTubeLink,
    user=Depends(get_current_user)  # AUTHENTICATED USER
):
    """
    Endpoint to process a YouTube link and return the summary.
    """

    if not youtube_link.youtube_link:
        raise HTTPException(status_code=400, detail="YouTube link is required!")

    # Validate YouTube link format
    if not YOUTUBE_URL_PATTERN.match(youtube_link.youtube_link):
        raise HTTPException(status_code=400, detail="Invalid YouTube link format!")

    # CHECK USAGE LIMITS
    allowed, reason = check_usage_allowed(user)

    if not allowed:
        raise HTTPException(status_code=429, detail=reason)

    # Process the YouTube link
    json_file_path = process_youtube_link(youtube_link.youtube_link)

    if not json_file_path or not os.path.exists(json_file_path):
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing the YouTube link."
        )

    try:
        with open(json_file_path, 'r') as json_file:
            summary_data = json.load(json_file)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read summary file: {str(e)}"
        )

    finally:
        # Always attempt to delete the file
        if os.path.exists(json_file_path):
            os.remove(json_file_path)

    # RECORD USAGE AFTER SUCCESS
    record_usage(user)

    return {
        "summary_points": summary_data.get('summary_points', [])
    }