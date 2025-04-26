from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import process_youtube_link
import os
import json
import re

app = FastAPI()

# Regex pattern to validate YouTube URLs
YOUTUBE_URL_PATTERN = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')

class YouTubeLink(BaseModel):
    youtube_link: str

@app.post("/process/")
async def process_youtube(youtube_link: YouTubeLink):
    """
    Endpoint to process a YouTube link and return the summary.

    Args:
        youtube_link (YouTubeLink): The YouTube video URL.

    Returns:
        dict: A dictionary containing the summary points.
    """
    if not youtube_link.youtube_link:
        raise HTTPException(status_code=400, detail="YouTube link is required!")

    # Validate YouTube link format
    if not YOUTUBE_URL_PATTERN.match(youtube_link.youtube_link):
        raise HTTPException(status_code=400, detail="Invalid YouTube link format!")

    # Process the YouTube link
    json_file_path = process_youtube_link(youtube_link.youtube_link)

    if not json_file_path or not os.path.exists(json_file_path):
        raise HTTPException(status_code=500, detail="An error occurred while processing the YouTube link.")

    try:
        with open(json_file_path, 'r') as json_file:
            summary_data = json.load(json_file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read summary file: {str(e)}")
    finally:
        # Always attempt to delete the file
        if os.path.exists(json_file_path):
            os.remove(json_file_path)

    return {"summary_points": summary_data.get('summary_points', [])}
