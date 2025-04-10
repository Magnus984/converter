from .word_to_ppt import word_to_ppt

from fastapi import APIRouter
api_version_one_router = APIRouter()
api_version_one_router.include_router(word_to_ppt)