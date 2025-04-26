import yt_dlp

def download_audio(link, output_format='wav', output_template='%(title)s.%(ext)s'):
    """
    Downloads audio from a YouTube link.

    Args:
        link (str): The YouTube video URL.
        output_format (str): The desired audio format (default is 'wav').
        output_template (str): The output file naming template.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio_format': output_format,
        'outtmpl': output_template,
        'quiet': False,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        print(f"Downloaded: {info.get('title', 'Unknown Title')}.{output_format}")

if __name__ == "__main__":
    # Example usage
    download_audio('https://www.youtube.com/watch?v=8HTapmpSZBE')