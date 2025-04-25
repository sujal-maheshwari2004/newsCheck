from flask import Flask, request, render_template, jsonify
from agent import process_youtube_link
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Render the homepage with a form to input the YouTube link."""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """
    Handle the form submission, process the YouTube link,
    and display the generated summary.
    """
    youtube_link = request.form.get('youtube_link')
    if not youtube_link:
        return "YouTube link is required!", 400

    # Process the YouTube link using agent.py
    json_file_path = process_youtube_link(youtube_link)

    if not json_file_path or not os.path.exists(json_file_path):
        return "An error occurred while processing the YouTube link.", 500

    # Read the generated JSON file
    with open(json_file_path, 'r') as json_file:
        summary_data = json.load(json_file)

    # Return the summary data to the user
    return render_template('result.html', summary='<br>'.join(summary_data['summary_points']))

if __name__ == '__main__':
    app.run(debug=True)