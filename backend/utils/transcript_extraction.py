from openai import OpenAI

def extract_transcript(api_key, audio_path, output_path):
    """
    Extracts a transcript from an audio file using OpenAI's Whisper model.

    Args:
        api_key (str): OpenAI API key.
        audio_path (str): Path to the audio file.
        output_path (str): Path to save the transcript.
    """
    client = OpenAI(api_key=api_key)

    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(transcription.text)

    print(f"Transcript saved to {output_path}")

if __name__ == "__main__":
    extract_transcript(api_key="------", audio_path="test.webm", output_path="transcript.txt")