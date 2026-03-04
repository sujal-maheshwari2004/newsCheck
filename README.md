# NewsCheck

**NewsCheck** is an AI-powered application that summarizes long-form YouTube news videos into concise bullet points.
Paste a YouTube link and receive key insights within seconds.

The system extracts the video transcript, processes it through a language model, and returns a structured summary for quick consumption.

---

## Features

* 🎥 **YouTube Link Processing** – Accepts standard YouTube video URLs
* 🧠 **AI Summarization** – Converts long transcripts into clear bullet points
* 🔐 **Authentication** – Magic-link login with token-based access
* ⚡ **Fast API Backend** – Built using FastAPI
* 🌐 **React Frontend** – Clean UI built with React + Vite
* 📊 **Structured Output** – Easy-to-read bullet summaries
* ☁️ **Cloud Deployment** – Ready for deployment on Render

---

## Tech Stack

### Frontend

* React
* Vite
* TailwindCSS

### Backend

* FastAPI
* Python

### AI / Processing

* OpenAI API
* YouTube transcript extraction

### Infrastructure

* Render (deployment)
* GitHub (version control)

---

## Project Structure

```
newsCheck
│
├── backend
│   ├── auth
│   ├── utils
│   ├── data
│   └── main.py
│
├── frontend
│   ├── src
│   │   ├── App.jsx
│   │   ├── Login.jsx
│   │   └── components
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## How It Works

1. User submits a YouTube link in the UI
2. Frontend sends request to the FastAPI backend
3. Backend extracts the video transcript
4. Transcript is processed using an LLM
5. AI generates concise bullet-point summaries
6. Summary is returned and displayed in the UI

---

## Local Development Setup

### 1. Clone the Repository

```
git clone https://github.com/sujal-maheshwari2004/newsCheck.git
cd newsCheck
```

---

### 2. Backend Setup

Create a virtual environment and install dependencies.

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key
```

Run the backend:

```
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### 3. Frontend Setup

```
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## Deployment

This project is designed to be deployed using **Render**.

### Backend

* Deploy FastAPI as a web service
* Set environment variables for API keys

### Frontend

* Deploy Vite build as a static site
* Configure API URL using environment variables

---

## Future Improvements

* Support for multiple video summarization styles
* Improved transcript segmentation
* User dashboard for history
* Caching summaries for repeated videos
* Improved rate limiting

---

## Author

**Sujal Maheshwari**

B.Tech CSE (AI & Data Science)
Graphic Era Deemed to be University

GitHub:
https://github.com/sujal-maheshwari2004

---

## License

This project is licensed under the MIT License.
