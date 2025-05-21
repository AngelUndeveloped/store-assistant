"""
Natural Language Processing Service Module

This module provides functionality for text generation using either LM Studio's local API
or Google's Gemini API. It handles text generation through HTTP requests to the local API
or direct calls to the Gemini API.
"""

import logging
from enum import Enum
from .nlp.lm_studio_provider import LMStudioProvider
from .nlp.gemini_provider import GeminiProvider

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ModelProvider(Enum):
    """Enum for available model providers"""
    LM_STUDIO = "lm_studio"
    GEMINI = "gemini"

def get_provider(provider: ModelProvider) -> LMStudioProvider | GeminiProvider:
    """
    Get the appropriate provider instance
    
    Args:
        provider (ModelProvider): The provider to use
        
    Returns:
        LMStudioProvider | GeminiProvider: The provider instance
        
    Raises:
        ValueError: If the provider is not supported
    """
    if provider == ModelProvider.LM_STUDIO:
        return LMStudioProvider()
    elif provider == ModelProvider.GEMINI:
        return GeminiProvider()
    else:
        raise ValueError(f"Unsupported model provider: {provider}")

def generate_response(prompt: str, provider: ModelProvider = ModelProvider.LM_STUDIO) -> str:
    """
    Generate a response using the specified provider
    
    Args:
        prompt (str): The input prompt
        provider (ModelProvider): The provider to use (default: LM_STUDIO)
        
    Returns:
        str: The generated response
        
    Raises:
        Exception: If there's an error generating the response
    """
    try:
        nlp_provider = get_provider(provider)
        return nlp_provider.generate_response(prompt)
    except Exception as e:
        logger .error("Error generating response: %s", str(e))
        raise
