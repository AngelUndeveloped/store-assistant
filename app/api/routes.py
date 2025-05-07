"""
API Routes Module for Store Assistant

This module defines the FastAPI routes for the Store Assistant application.
It provides endpoints for:
- Health check and API status verification
- Speech-to-text conversion using the Whisper model

The module uses FastAPI's APIRouter for route management and includes
endpoints for handling file uploads and audio processing.
"""

from fastapi import APIRouter, UploadFile, File
from app.services.stt_service import transcribe_audio

router = APIRouter()

@router.get("/")
async def root():
    """
    Health check endpoint to verify API status.
    
    Returns:
        dict: A dictionary containing a status message indicating the API is running.
        Example: {"message": "Store Assistant API is running."}
    """
    return {"message": "Store Assistant API is running."}

@router.post("/speech-to-text/")
async def speech_to_text(audio: UploadFile = File(...)):
    """
    Endpoint to convert speech from an audio file to text.
    
    Args:
        audio (UploadFile): The audio file to be transcribed. Must be a valid audio file format.
            The file is received as a multipart form data upload.
    
    Returns:
        dict: A dictionary containing either:
            - On success: {"text": str} with the transcribed text
            - On error: {"error": str} with the error message
    
    Note:
        This endpoint uses the Whisper model for speech-to-text conversion.
        The audio file should be in a format supported by Whisper (e.g., .wav, .mp3, .webm).
    """
    try:
        text = transcribe_audio(audio)
        return {"text": text}
    except (IOError, ValueError) as e:
        return {"error": str(e)}
