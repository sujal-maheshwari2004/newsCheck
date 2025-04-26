import json

def convert_summary_to_json(summary_path, output_path):
    """
    Converts a text summary into a JSON format.

    Args:
        summary_path (str): Path to the summary text file.
        output_path (str): Path to save the JSON file.
    """
    with open(summary_path, "r", encoding="utf-8") as file:
        summary_text = file.read()

    points = [
        line.strip()[2:].strip()  # remove '--' and leading/trailing whitespace
        for line in summary_text.splitlines()
        if line.strip().startswith('--')
    ]

    summary_json = {
        "summary_points": points
    }

    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(summary_json, json_file, indent=4, ensure_ascii=False)

    print(f"Parsed summary saved to {output_path}")

if __name__ == "__main__":
    convert_summary_to_json(summary_path="summary.txt", output_path="news_summary.json")