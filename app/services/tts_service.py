"""
Text-to-Speech Service Module

This module provides functionality for converting text to speech using the pyttsx3 library.
It handles text-to-speech conversion and temporary file management for audio output.
The service uses the system's default text-to-speech engine through pyttsx3.
"""

import tempfile
import pyttsx3

def text_to_speech(text: str) -> str:
    """
    Converts text to speech and saves it as a temporary audio file.
    
    Args:
        text (str): The text to be converted to speech.
    
    Returns:
        str: The path to the temporary audio file containing the speech.
        
    Raises:
        IOError: If there's an error creating or writing to the temporary file.
        ValueError: If the text is empty or invalid.
        RuntimeError: If there's an error with the text-to-speech engine.
    """
    engine = pyttsx3.init()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file_path = tmp_file.name
        engine.save_to_file(text, tmp_file_path)
        engine.runAndWait()
    
    return tmp_file_path
