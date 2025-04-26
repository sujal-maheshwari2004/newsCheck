from utils.extract_audio import download_audio
from utils.transcript_extraction import extract_transcript
from utils.summarizer import summarize_transcript
from utils.jsonify import convert_summary_to_json
import dotenv
import os
import shutil

# Load environment variables from .env file
dotenv.load_dotenv()

TEMP_FOLDER = "temp"

def ensure_temp_folder():
    """Ensures the temp folder exists."""
    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)

def clean_temp_folder():
    """Deletes all files and the temp folder."""
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)

def process_youtube_link(youtube_link):
    """
    Processes a YouTube link to extract audio, generate a transcript, summarize it, and convert the summary to JSON.

    Args:
        youtube_link (str): The YouTube video URL.

    Returns:
        str: Path to the generated JSON file.
    """
    try:
        ensure_temp_folder()

        # Step 1: Download audio from YouTube
        audio_format = "webm"
        audio_output_template = os.path.join(TEMP_FOLDER, "downloaded_audio.%(ext)s")
        print("Downloading audio...")
        download_audio(link=youtube_link, output_format=audio_format, output_template=audio_output_template)

        # Step 2: Extract transcript from the downloaded audio
        audio_path = os.path.join(TEMP_FOLDER, "downloaded_audio.webm")  # Ensure this matches the downloaded file
        transcript_path = os.path.join(TEMP_FOLDER, "transcript.txt")
        
        # Retrieve API key from environment variables
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key is missing in the .env file!")

        print("Extracting transcript...")
        extract_transcript(api_key=api_key, audio_path=audio_path, output_path=transcript_path)

        # Step 3: Summarize the transcript
        summary_path = os.path.join(TEMP_FOLDER, "news_summary.txt")
        print("Summarizing transcript...")
        summarize_transcript(api_key=api_key, transcript_path=transcript_path, output_path=summary_path)

        # Step 4: Convert the summary to JSON
        json_output_path = "news_summary.json"
        print("Converting summary to JSON...")
        convert_summary_to_json(summary_path=summary_path, output_path=json_output_path)

        print("Processing completed successfully!")
        return json_output_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Clean up the temp folder
        clean_temp_folder()
