from fastapi import APIRouter, UploadFile, File
from app.services.stt_service import transcribe_audio

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Store Assistant API is running."}

@router.post("/speech-to-text/")
async def speech_to_text(audio: UploadFile = File(...)):
    try:
        text = transcribe_audio(audio)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/speech-to-text/")
async def speech_to_text_get():
    return {"message": "Speech to text API is running."}