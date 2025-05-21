"""
Main Application Module

This module initializes and configures the FastAPI application for the Store Assistant.
It sets up the main application instance and includes all necessary routers.
The application provides an API for store management with speech-to-text capabilities.
"""

from fastapi import FastAPI
from app.api.routes import router as stt_router

app = FastAPI(
    title="AI Store Assistant",
              description="AI Store Assistant is a tool that helps you manage your store"
              )

# Include the speech-to-text router
app.include_router(router=stt_router)
