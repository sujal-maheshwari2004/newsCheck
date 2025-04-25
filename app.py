from flask import Flask, request, render_template
from agent import process_youtube_link
import os
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    error = None

    if request.method == 'POST':
        youtube_link = request.form.get('youtube_link')
        if not youtube_link:
            error = "YouTube link is required!"
        else:
            json_file_path = process_youtube_link(youtube_link)

            if not json_file_path or not os.path.exists(json_file_path):
                error = "An error occurred while processing the YouTube link."
            else:
                with open(json_file_path, 'r') as json_file:
                    summary_data = json.load(json_file)
                    summary = summary_data.get('summary_points', [])

    return render_template('index.html', summary=summary, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
