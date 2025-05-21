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
from fastapi.responses import FileResponse
from app.services.nlp_service import ModelProvider, generate_response
from app.services.stt_service import transcribe_audio
from app.services.tts_service import text_to_speech

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

@router.post("/speech-to-text")
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

@router.post("/text-to-speech")
async def generate_audio(text: str):
    """
    Endpoint to convert text to speech.
    
    Args:
        text (str): The text to be converted to speech.
    
    Returns:
        dict: A dictionary containing either:
            - On success: {"audio": bytes} with the audio data
            - On error: {"error": str} with the error message
    
    Note:
        This endpoint converts the provided text into speech audio.
        The audio is returned as binary data that can be played or saved as an audio file.
    """
    try:
        audio_path = text_to_speech(text)
        return FileResponse(path=audio_path, media_type="audio/mp3", filename="response.mp3")
    except (IOError, ValueError) as e:
        return {"error": str(e)}

@router.post("/nlp")
async def chat_with_assistant(prompt: str, provider: str="lm_studio") -> dict:
    """
    Endpoint to generate a response using the NLP model.
    
    Args:
        prompt (str): The text prompt to generate a response for.
        provider (str): The model provider to use. Options: "lm_studio" or "gemini"
            (default: "lm_studio")
    
    Returns:
        dict: A dictionary containing either:
            - On success: {"response": str} with the generated text response
            - On error: {"error": str} with the error message
    
    Note:
        This endpoint supports multiple model providers:
        - LM Studio: Local model inference (requires LM Studio to be running)
        - Gemini: Google's Gemini API (requires GEMINI_API_KEY in environment)
    """
    try:
        model_provider = ModelProvider(provider.lower())
        response = generate_response(prompt, provider=model_provider)
        return {"response": response}
    except ValueError as e:
        return {"error": f"Invalid provider: {str(e)}"}
    except RuntimeError as e:
        return {"error": f"Error generating response: {str(e)}"}
    except ConnectionError as e:
        return {"error": f"Failed to connect to model service: {str(e)}"}
    except TimeoutError as e:
        return {"error": f"Request timed out: {str(e)}"}
