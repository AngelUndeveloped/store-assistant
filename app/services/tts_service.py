import pyttsx3
import tempfile
import os

def text_to_speech(text: str) -> str:
    engine = pyttsx3.init()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file_path = tmp_file.name
        engine.save_to_file(text, tmp_file_path)
        engine.runAndWait()
    
    return tmp_file_path