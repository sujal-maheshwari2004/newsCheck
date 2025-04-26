# 📰 newsCheck

## Usage

1. **Start the Backend**  
   - Navigate to the `backend/` folder.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Create a `.env` file with your OpenAI API key:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```
   - Run the FastAPI server:
     ```bash
     uvicorn main:app --reload
     ```

2. **Start the Frontend**  
   - Navigate to the `frontend/` folder.
   - Install dependencies:
     ```bash
     npm install
     ```
   - Run the development server:
     ```bash
     npm run dev
     ```

3. **Using the App**  
   - Open the frontend at `http://localhost:5173`.
   - Enter a YouTube news video link.
   - Click submit.
   - The app will extract, transcribe, and summarize the video into 5 key points.

---
