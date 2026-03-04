from utils.extract_audio import download_audio
from utils.transcript_extraction import extract_transcript
from utils.summarizer import summarize_transcript
from utils.jsonify import convert_summary_to_json

import dotenv
import os
import shutil

dotenv.load_dotenv()

TEMP_FOLDER = "temp"


def ensure_temp_folder():
    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)


def clean_temp_folder():
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)


def ensure_cookie_file():
    """
    Creates cookies.txt from environment variable if available.
    """
    cookies = os.getenv("YOUTUBE_COOKIES")

    if cookies:
        with open("cookies.txt", "w") as f:
            f.write(cookies)


def process_youtube_link(youtube_link):
    """
    Full pipeline:
    youtube -> audio -> transcript -> summary -> json
    """

    try:
        ensure_cookie_file()
        ensure_temp_folder()

        # Step 1 Download audio
        audio_format = "wav"
        audio_output_template = os.path.join(TEMP_FOLDER, "downloaded_audio.%(ext)s")

        print("Downloading audio...")

        download_audio(
            link=youtube_link,
            output_format=audio_format,
            output_template=audio_output_template
        )

        audio_path = os.path.join(TEMP_FOLDER, "downloaded_audio.wav")

        transcript_path = os.path.join(TEMP_FOLDER, "transcript.txt")

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY missing.")

        # Step 2 Transcription
        print("Extracting transcript...")

        extract_transcript(
            api_key=api_key,
            audio_path=audio_path,
            output_path=transcript_path
        )

        # Step 3 Summarization
        summary_path = os.path.join(TEMP_FOLDER, "news_summary.txt")

        print("Summarizing transcript...")

        summarize_transcript(
            api_key=api_key,
            transcript_path=transcript_path,
            output_path=summary_path
        )

        # Step 4 Convert to JSON
        json_output_path = "news_summary.json"

        print("Converting summary to JSON...")

        convert_summary_to_json(
            summary_path=summary_path,
            output_path=json_output_path
        )

        print("Processing completed successfully.")

        return json_output_path

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    finally:
        clean_temp_folder()
