import streamlit as st
import tempfile
import os
import re
import wave
from datetime import datetime

st.header("Transcript")
st.caption("Upload a .wav audio file and get a transcript using OpenAI Whisper (small model, runs locally).")

uploaded_file = st.file_uploader(
    "Drag & drop or browse a .wav file",
    type=["wav"],
    accept_multiple_files=False,
)

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Transcribe"):
        with st.spinner("Loading Whisper model and transcribing..."):
            import whisper

            model = whisper.load_model("small")

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name

            try:
                # Get audio duration
                with wave.open(tmp_path, "r") as wf:
                    frames = wf.getnframes()
                    rate = wf.getframerate()
                    duration_secs = int(frames / rate)

                result = model.transcribe(tmp_path)
                transcript = result["text"].strip()
            finally:
                os.unlink(tmp_path)

        # Extract timestamp from filename or use current time
        match = re.search(r"(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})", uploaded_file.name)
        if match:
            date_str = f"{match.group(1)}-{match.group(2)}-{match.group(3)} {match.group(4)}:{match.group(5)}:{match.group(6)}"
        else:
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format audio duration
        hours, remainder = divmod(duration_secs, 3600)
        minutes, secs = divmod(remainder, 60)
        duration_str = f"{hours:02d}:{minutes:02d}:{secs:02d}"

        # Build output
        output = f"Date: {date_str}\nAudio Length: {duration_str}\n\nTranscript:\n{transcript}"

        st.success("Transcription complete!")
        st.code(output, language=None, wrap_lines=True)
