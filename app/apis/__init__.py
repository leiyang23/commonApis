from fastapi import APIRouter

tool_router = APIRouter(prefix="/tool")

from .weather import weather
