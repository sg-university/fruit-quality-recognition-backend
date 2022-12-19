from fastapi import APIRouter
from pydantic.types import UUID, List

from app.core.models.entities.Detection import Detection
from app.core.usecases.detection import crud_usecase
from app.outer.interfaces.controllers.requests.detection_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.detection_controller.patch_one_request import PatchOneRequest
from app.outer.interfaces.controllers.responses.Content import Content

router = APIRouter(prefix="/detections")


@router.get("/", response_model=Content[List[Detection]])
async def read_all() -> Content[List[Detection]]:
    content = Content[List[Detection]](
        message="Read all detection succeed.",
        data=crud_usecase.read_all()
    )
    return content


@router.get("/{id}", response_model=Content[Detection])
async def read_one_by_id(id: UUID) -> Content[Detection]:
    content = Content[Detection](
        message="Read one detection succeed.",
        data=crud_usecase.read_one_by_id(id)
    )
    return content


@router.post("/", response_model=Content[Detection])
async def create_one(request: CreateOneRequest) -> Content[Detection]:
    content = Content[Detection](
        message="Create one detection succeed.",
        data=crud_usecase.create_one(request)
    )
    return content


@router.post("/many", response_model=Content[Detection])
async def create_many(requests: List[CreateOneRequest]) -> Content[List[Detection]]:
    content = Content[List[Detection]](
        message="Create many detection succeed.",
        data=crud_usecase.create_many(requests)
    )
    return content


@router.patch("/{id}", response_model=Content[Detection])
async def patch_one_by_id(id: UUID, request: PatchOneRequest) -> Content[Detection]:
    content = Content[Detection](
        message="Patch one detection succeed.",
        data=crud_usecase.patch_one_by_id(id, request)
    )
    return content


@router.delete("/{id}", response_model=Content[Detection])
async def delete_one_by_id(id: UUID) -> Content[Detection]:
    content = Content[Detection](
        message="Delete one detection succeed.",
        data=crud_usecase.delete_one_by_id(id)
    )
    return content
