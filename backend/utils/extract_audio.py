import yt_dlp
import os


def download_audio(link, output_format="wav", output_template="%(title)s.%(ext)s"):
    """
    Downloads audio from a YouTube link and returns the downloaded file path.
    """

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "noplaylist": True,
        "quiet": True,

        # retry logic
        "retries": 10,
        "fragment_retries": 10,
        "skip_unavailable_fragments": True,

        # network robustness
        "nocheckcertificate": True,
        "geo_bypass": True,

        # prevent ipv6 issues on cloud hosts
        "source_address": "0.0.0.0",

        # browser-like request headers
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        },

        # extractor tweaks for youtube throttling
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        },

        # convert audio using ffmpeg
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": output_format,
            "preferredquality": "192",
        }],
    }

    # Only use cookies if they exist
    if os.path.exists("cookies.txt"):
        ydl_opts["cookiefile"] = "cookies.txt"
        print("Using cookies.txt for YouTube authentication")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        print("Starting YouTube download...")

        info = ydl.extract_info(link, download=True)

        downloaded_file = ydl.prepare_filename(info)

        # Replace extension if ffmpeg converted it
        downloaded_file = os.path.splitext(downloaded_file)[0] + f".{output_format}"

        print(f"Downloaded audio: {downloaded_file}")

        return downloaded_file


if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=8HTapmpSZBE")
