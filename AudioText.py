import streamlit as st
from openai import OpenAI
import tempfile


st.set_page_config(page_title="Audio to Text Transcriber", page_icon="🎙️")

# Sidebar for API Key
st.sidebar.title("🔑 OpenAI API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

# File uploader
st.title("🎧 Audio to Text Transcription using")
uploaded_file = st.file_uploader("Upload an MP3 file (Max 2MB)", type=["mp3"])

# Size check
if uploaded_file is not None and uploaded_file.size > 2 * 1024 * 1024:
    st.error("File size exceeds 2MB limit.")
    uploaded_file = None

if uploaded_file and api_key:
    with st.spinner("Transcribing..."):
        # Save to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            client = OpenAI(api_key=api_key)
            with open(tmp_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="gpt-4o-transcribe",
                    file=audio_file
                )
            st.success("Transcription Completed!")
            st.text_area("📝 Transcribed Text:", transcription.text, height=300)
        except Exception as e:
            st.error(f"Error: {str(e)}")
else:
    st.info("Please upload an MP3 file and enter your OpenAI API key.")