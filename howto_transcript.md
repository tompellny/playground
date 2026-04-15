# How-to: Transcribe an Audio File

**Application:** Playground (Streamlit App)

## Start the App

- Open Terminal
- `cd ~/LOCALDATA/DEV/Playground`
- `source .venv/bin/activate`
- `streamlit run streamlit_app.py`
- The app opens in your browser at http://localhost:8501

## Transcribe

- Navigate to the **Transcript** page
- Drag & drop a `.wav` audio file into the upload area (or click "Browse files")
- Click **Transcribe**
- Wait for the transcription to complete (approx. 10–15 sec per audio minute on Apple Silicon)
- The output shows date, audio length, and transcript text
- Click the **copy icon** (top right of the text box) to copy the result

## Stop the App

- Go back to Terminal
- Press `Ctrl+C` twice to stop the server
- Type `deactivate` to exit the virtual environment
