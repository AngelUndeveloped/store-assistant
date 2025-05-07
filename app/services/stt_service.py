"""
Speech-to-Text Service Module

This module provides functionality for converting speech to text using the Whisper model.
It handles audio file processing and transcription through OpenAI's Whisper model.
The module uses a base model for transcription, which can be changed if needed.
"""

import tempfile
import whisper
from fastapi import UploadFile

model = whisper.load_model("base") # change model if needed

def transcribe_audio(file: UploadFile) -> str:
    """
    Transcribes audio from an uploaded file to text using the Whisper model.
    
    Args:
        file (UploadFile): The audio file to be transcribed. Must be a valid audio format
            supported by Whisper (e.g., .wav, .mp3, .webm).
    
    Returns:
        str: The transcribed text from the audio file.
        
    Raises:
        IOError: If there's an error reading or writing the temporary file.
        ValueError: If the audio file format is invalid or unsupported.
        KeyError: If the transcription result doesn't contain the expected 'text' key.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp_file:
        tmp_file.write(file.file.read())
        tmp_file_path = tmp_file.name

    result = model.transcribe(tmp_file_path)
    return result["text"]
