import whisper
from fastapi import UploadFile
import tempfile

model = whisper.load_model("base") # change model if needed

def transcribe_audio(file:UploadFile) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp_file:
        tmp_file.write(file.file.read())
        tmp_file_path = tmp_file.name
    
    result = model.transcribe(tmp_file_path)
    return result["text"]