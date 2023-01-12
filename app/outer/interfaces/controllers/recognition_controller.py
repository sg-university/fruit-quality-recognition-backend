from fastapi import APIRouter
from pydantic.types import UUID, List

from app.inner.models.entities.Recognition import Recognition
from app.inner.usecases.recognition import crud_usecase
from app.outer.interfaces.controllers.requests.recognition_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.recognition_controller.patch_one_request import PatchOneRequest
from app.outer.interfaces.controllers.responses.Content import Content

router = APIRouter(prefix="/recognitions")


@router.get("/", response_model=Content[List[Recognition]])
async def read_all() -> Content[List[Recognition]]:
    content = Content[List[Recognition]](
        message="Read all recognition succeed.",
        data=crud_usecase.read_all()
    )
    return content


@router.get("/{id}", response_model=Content[Recognition])
async def read_one_by_id(id: UUID) -> Content[Recognition]:
    content = Content[Recognition](
        message="Read one recognition succeed.",
        data=crud_usecase.read_one_by_id(id)
    )
    return content


@router.post("/", response_model=Content[Recognition])
async def create_one(request: CreateOneRequest) -> Content[Recognition]:
    content = Content[Recognition](
        message="Create one recognition succeed.",
        data=crud_usecase.create_one(request)
    )
    return content


@router.post("/many", response_model=Content[List[Recognition]])
async def create_many(request: List[CreateOneRequest]) -> Content[List[Recognition]]:
    content = Content[List[Recognition]](
        message="Create many recognition succeed.",
        data=crud_usecase.create_many(request)
    )
    return content


@router.patch("/{id}", response_model=Content[Recognition])
async def patch_one_by_id(id: UUID, request: PatchOneRequest) -> Content[Recognition]:
    content = Content[Recognition](
        message="Patch one recognition succeed.",
        data=crud_usecase.patch_one_by_id(id, request)
    )
    return content


@router.delete("/{id}", response_model=Content[Recognition])
async def delete_one_by_id(id: UUID) -> Content[Recognition]:
    content = Content[Recognition](
        message="Delete one recognition succeed.",
        data=crud_usecase.delete_one_by_id(id)
    )
    return content
