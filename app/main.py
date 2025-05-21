"""
Main Application Module

This module initializes and configures the FastAPI application for the Store Assistant.
It sets up the main application instance and includes all necessary routers.
The application provides an API for store management with speech-to-text capabilities.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as stt_router

app = FastAPI(
    title="AI Store Assistant",
    description="AI Store Assistant is a tool that helps you manage your store"
)

# Configure CORS
origins = [
    "http://192.168.0.220:3000",  # Your frontend URL
    "http://localhost:3000",       # Local development
    "http://127.0.0.1:3000",      # Alternative local URL
    "http://localhost:8000",
    "http://localhost:8000/nlp",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the speech-to-text router
app.include_router(router=stt_router)
