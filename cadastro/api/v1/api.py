from fastapi import APIRouter

from api.v1.endpoints import processo

api_router = APIRouter()
api_router.include_router(processo.router, tags=["processo"])