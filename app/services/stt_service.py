import whisper
from fastapi import UploadFile
import tempfile

model = whisper.load_model("base") # change model if needed

# def transcribe_audio(file:UploadFile)