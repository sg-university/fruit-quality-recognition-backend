from fastapi import APIRouter

from app.outer.interfaces.controllers import recognition_controller, image_controller

api_router = APIRouter()

api_router.include_router(recognition_controller.router)
api_router.include_router(image_controller.router)
