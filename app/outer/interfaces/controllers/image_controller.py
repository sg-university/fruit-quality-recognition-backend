from fastapi import APIRouter
from pydantic.types import UUID, List

from app.core.models.entities.Image import Image
from app.core.usecases.image import crud_usecase

router = APIRouter(prefix="/images")


@router.get("/", response_model=List[Image])
async def read_all() -> List[Image]:
    return crud_usecase.read_all()


@router.get("/{id}", response_model=Image)
async def read_one_by_id(id: UUID) -> Image:
    return crud_usecase.read_one_by_id(id)


@router.post("/", response_model=Image)
async def create_one(entity: Image) -> Image:
    return crud_usecase.create_one(entity)


@router.patch("/{id}", response_model=Image)
async def patch_one_by_id(id: UUID, entity: Image) -> Image:
    return crud_usecase.patch_one_by_id(id, entity)


@router.delete("/{id}", response_model=Image)
async def delete_one_by_id(id: UUID) -> Image:
    return crud_usecase.delete_one_by_id(id)
