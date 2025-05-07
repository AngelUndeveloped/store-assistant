from transformers import pipeline

chatbot = pipeline("text-generation", model="google/gemini-2.5-flash")

def generate_response(prompt: str) -> str:
    result = chatbot(prompt, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]