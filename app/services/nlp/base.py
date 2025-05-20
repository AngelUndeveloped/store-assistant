"""
Base class for NLP providers
"""
from abc import ABC, abstractmethod

class NLPProvider(ABC):
    """Abstract base class for NLP providers"""
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response for the given prompt
        
        Args:
            prompt (str): The input prompt
            
        Returns:
            str: The generated response
            
        Raises:
            Exception: If there's an error generating the response
        """
        pass 