import yt_dlp
import os


def download_audio(link, output_format="wav", output_template="%(title)s.%(ext)s"):
    """
    Downloads audio from a YouTube link and returns the downloaded file path.

    Args:
        link (str): The YouTube video URL
        output_format (str): Desired audio format (wav/mp3/etc)
        output_template (str): Output filename template
    """

    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        "outtmpl": output_template,
        "noplaylist": True,
        "quiet": True,

        # retry logic
        "retries": 10,
        "fragment_retries": 10,

        # network robustness
        "nocheckcertificate": True,
        "geo_bypass": True,
        "source_address": "0.0.0.0",

        # reduce bot detection
        "sleep_interval": 2,
        "max_sleep_interval": 5,

        # browser-like headers
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        },

        # YouTube extractor config
        "extractor_args": {
            "youtube": {
                "player_client": ["web"]
            }
        },

        # convert audio with ffmpeg
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": output_format,
            "preferredquality": "192",
        }],
    }

    # Use cookies if they exist
    if os.path.exists("cookies.txt"):
        ydl_opts["cookiefile"] = "cookies.txt"
        print("Using cookies.txt for authentication")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        print("Starting YouTube audio download...")

        info = ydl.extract_info(link, download=True)

        # original filename from yt-dlp
        downloaded_file = ydl.prepare_filename(info)

        # change extension after ffmpeg conversion
        downloaded_file = os.path.splitext(downloaded_file)[0] + f".{output_format}"

        print(f"Downloaded audio file: {downloaded_file}")

        return downloaded_file


if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=8HTapmpSZBE")
