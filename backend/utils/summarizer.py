from openai import OpenAI

def summarize_transcript(api_key, transcript_path, output_path):
    """
    Summarizes a transcript using OpenAI's GPT model.

    Args:
        api_key (str): OpenAI API key.
        transcript_path (str): Path to the transcript file.
        output_path (str): Path to save the summary.
    """
    client = OpenAI(api_key=api_key)

    with open(transcript_path, "r", encoding="utf-8") as file:
        text = file.read()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a skilled news editor and analyst. You specialize in distilling video news transcripts "
                "into concise summaries that preserve factual accuracy, highlight the most critical developments, "
                "and convey the essence of the story in a clear, neutral tone."
            )
        },
        {
            "role": "user",
            "content": (
                f"The following is a raw transcript from a news video. Your task is to extract and summarize the "
                f"**five most important and newsworthy points** from this transcript. Focus on key events, figures, "
                f"decisions, statements, or consequences mentioned. Ensure each point is clear, concise, and captures "
                f"the core of what was said.\n\n"
                f"- Present your summary in a **bullet-point format**.\n"
                f"- Each point must begin with a new line and a double dash `--`.\n"
                f"- Limit your summary to **no more than 5 sentences total**.\n"
                f"- Avoid unnecessary details, filler, or personal opinions.\n\n"
                f"--- Begin Transcript ---\n{text}\n--- End Transcript ---"
            )
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3
    )

    summary = response.choices[0].message.content.strip()

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(summary)

    print(f"Summary saved to {output_path}")

if __name__ == "__main__":
    summarize_transcript(api_key="---", transcript_path="transcript.txt", output_path="news_summary.txt")