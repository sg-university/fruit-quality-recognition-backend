from fastapi import APIRouter
from pydantic.types import UUID, List

from app.core.models.entities.Detection import Detection
from app.core.usecases.detection import crud_usecase

router = APIRouter(prefix="/detections")


@router.get("/", response_model=List[Detection])
async def read_all() -> List[Detection]:
    return crud_usecase.read_all()


@router.get("/{id}", response_model=Detection)
async def read_one_by_id(id: UUID) -> Detection:
    return crud_usecase.read_one_by_id(id)


@router.post("/", response_model=Detection)
async def create_one(entity: Detection) -> Detection:
    return crud_usecase.create_one(entity)


@router.patch("/{id}", response_model=Detection)
async def patch_one_by_id(id: UUID, entity: Detection) -> Detection:
    return crud_usecase.patch_one_by_id(id, entity)


@router.delete("/{id}", response_model=Detection)
async def delete_one_by_id(id: UUID) -> Detection:
    return crud_usecase.delete_one_by_id(id)
