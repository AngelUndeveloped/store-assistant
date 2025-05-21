"""
Gemini API provider implementation
"""
import os
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types
from app.services.nlp.base import NLPProvider

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

class GeminiProvider(NLPProvider):
    """Gemini API provider implementation"""

    def __init__(self, model: str = None, temperature: float = 0.7):
        """
        Initialize the Gemini provider
        
        Args:
            model (str): The model to use (default: from environment variable GEMINI_MODEL)
            temperature (float): The temperature for generation (default: 0.7)
        """
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-pro")
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
            logging.debug("Generating response with Gemini model: %s", self.model)

            contents = [
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=prompt)],
                )
            ]

            generate_content_config = types.GenerateContentConfig(
                temperature=self.temperature,
                response_mime_type="text/plain",
            )

            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=generate_content_config,
            )

            logger.debug("Gemini response received successfully")
            return response.text
        except Exception as e:
            logging.error("Error generating response with Gemini: %s", str(e))
            raise RuntimeError(f"Error generating response with Gemini: {str(e)}") from e
