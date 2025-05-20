"""
Gemini API provider implementation
"""
import os
import logging
from google import genai
from google.genai import types
from .base import NLPProvider

logger = logging.getLogger(__name__)

class GeminiProvider(NLPProvider):
    """Gemini API provider implementation"""
    
    def __init__(self, model: str = "gemini-pro", temperature: float = 0.7):
        """
        Initialize the Gemini provider
        
        Args:
            model (str): The model to use (default: "gemini-pro")
            temperature (float): The temperature for generation (default: 0.7)
        """
        self.model = model
        self.temperature = temperature
        self.client = self._initialize_client()
        
    def _initialize_client(self) -> genai.Client:
        """Initialize the Gemini client"""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set")
        return genai.Client(api_key=api_key)
    
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response using the Gemini API
        
        Args:
            prompt (str): The input prompt
            
        Returns:
            str: The generated response
            
        Raises:
            Exception: If there's an error generating the response
        """
        try:
            contents = [
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=prompt)],
                ),
            ]
            
            generate_content_config = types.GenerateContentConfig(
                temperature=self.temperature,
                response_mime_type="text/plain",
            )
            
            logger.debug(f"Generating response with Gemini model: {self.model}")
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=generate_content_config,
            )
            
            logger.debug("Gemini response received successfully")
            return response.text
            
        except Exception as e:
            logger.error(f"Error generating response with Gemini: {str(e)}")
            raise RuntimeError(f"Error generating response with Gemini: {str(e)}") from e 