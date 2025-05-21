"""
LM Studio provider implementation
"""
import os
import logging
import requests
from .base import NLPProvider

logger = logging.getLogger(__name__)

class LMStudioProvider(NLPProvider):
    """LM Studio provider implementation"""
    
    def __init__(self, api_url: str = None, temperature: float = 0.7, max_tokens: int = 1000):
        """
        Initialize the LM Studio provider
        
        Args:
            api_url (str): The LM Studio API URL (default: from environment)
            temperature (float): The temperature for generation (default: 0.7)
            max_tokens (int): Maximum tokens to generate (default: 1000)
        """
        self.api_url = api_url or os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1/chat/completions")
        self.temperature = temperature
        self.max_tokens = max_tokens
        
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response using the LM Studio API
        
        Args:
            prompt (str): The input prompt
            
        Returns:
            str: The generated response
            
        Raises:
            Exception: If there's an error generating the response
        """
        try:
            headers = {
                "Content-Type": "application/json"
            }

            data = {
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": self.temperature,
                "max_tokens": self.max_tokens
            }

            logger.debug(f"Attempting to connect to LM Studio at: {self.api_url}")
            logger.debug(f"Request data: {data}")
            
            response = requests.post(
                url=self.api_url,
                headers=headers,
                json=data,
                timeout=10
            )
            
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