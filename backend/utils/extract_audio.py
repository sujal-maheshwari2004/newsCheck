import yt_dlp


def download_audio(link, output_format='wav', output_template='%(title)s.%(ext)s'):
    """
    Downloads audio from a YouTube link.

    Args:
        link (str): The YouTube video URL.
        output_format (str): Desired audio format.
        output_template (str): Output file naming template.
    """

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "noplaylist": True,
        "quiet": True,

        # cookies help bypass some youtube restrictions
        "cookiefile": "cookies.txt",

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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
        },

        # extractor tweaks for youtube throttling
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        },

        # postprocess audio
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": output_format,
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        print(f"Downloaded: {info.get('title', 'Unknown Title')}.{output_format}")


if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=8HTapmpSZBE")
