"""
Natural Language Processing Service Module

This module provides functionality for text generation using LM Studio's local API.
It connects to a locally running LM Studio instance for generating responses to user prompts.
The service handles text generation through HTTP requests to the local API.
"""

import requests
import logging
import base64
import os
from google import genai
from google.genai import types

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# For local developement, use lm studio api endpoint, validate lm studio server settings
API_URL = "http://192.168.0.220:1234/v1/chat/completions"

# For production, use gemini api endpoint



def generate_response(prompt: str, model: str) -> str:
    """
    Generates a text response based on the given prompt using LM Studio's local API.
    
    Args:
        prompt (str): The input text prompt to generate a response for.
    
    Returns:
        str: The generated text response.
        
    Raises:
        ConnectionError: If unable to connect to LM Studio API.
        ValueError: If the prompt is empty or invalid.
        RuntimeError: If there's an error with the API response.
    """
    try:
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        logger.debug(f"Attempting to connect to LM Studio at: {API_URL}")
        logger.debug(f"Request data: {data}")
        
        response = requests.post(url=API_URL, headers=headers, json=data, timeout=10)
        logger.debug(f"Response status code: {response.status_code}")
        logger.debug(f"Response content: {response.text}")
        
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.ConnectionError as exc:
        logger.error(f"Connection error: {str(exc)}")
        raise ConnectionError("Could not connect to LM Studio API. Please ensure LM Studio is running and accessible.") from exc
    except (KeyError, IndexError) as e:
        logger.error(f"Unexpected API response format: {str(e)}")
        raise RuntimeError(f"Unexpected API response format: {str(e)}") from e
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        raise RuntimeError(f"API request failed: {str(e)}") from e
