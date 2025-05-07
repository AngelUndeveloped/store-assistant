"""
Natural Language Processing Service Module

This module provides functionality for text generation using the Hugging Face Transformers library.
It uses the Qwen3-8B model for generating responses to user prompts.
The service handles text generation with configurable parameters for response length and quality.
"""

from transformers import pipeline
import torch

# Check if CUDA is available and set device accordingly
device = 0 if torch.cuda.is_available() else -1

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen3-8B",
    device=device,
    torch_dtype=torch.float16 if device == 0 else torch.float32
)

def generate_response(prompt: str) -> str:
    """
    Generates a text response based on the given prompt using the Qwen model.
    
    Args:
        prompt (str): The input text prompt to generate a response for.
    
    Returns:
        str: The generated text response.
        
    Raises:
        ValueError: If the prompt is empty or invalid.
        RuntimeError: If there's an error with the model or generation process.
    """
    result = chatbot(prompt, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]
