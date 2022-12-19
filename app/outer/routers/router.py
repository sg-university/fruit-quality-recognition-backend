from fastapi import APIRouter

from app.outer.interfaces.controllers import detection_controller, image_controller

api_router = APIRouter()

api_router.include_router(detection_controller.router)
api_router.include_router(image_controller.router)
