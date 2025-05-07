from fastapi import FastAPI
from fastapi import APIRouter
from app.api.routes import router as stt_router

app = FastAPI(title="AI Store Assistant", description="AI Store Assistant is a tool that helps you manage your store")
app.include_router(router=stt_router)
