"""
Natural Language Processing Service Module

This module provides functionality for text generation using LM Studio's local API.
It connects to a locally running LM Studio instance for generating responses to user prompts.
The service handles text generation through HTTP requests to the local API.
"""

import requests

# LM Studio API endpoint (default when running locally)
API_URL = "http://localhost:1234/v1/chat/completions"

def generate_response(prompt: str) -> str:
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
            "max_tokens": 100
        }

        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.ConnectionError as exc:
        raise ConnectionError("Could not connect to LM Studio API.") from exc
    except (KeyError, IndexError) as e:
        raise RuntimeError(f"Unexpected API response format: {str(e)}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {str(e)}") from e
