from pydantic.types import UUID, List

from app.core.models.entities.Image import Image
from app.outer.repositories import image_repository


def read_all() -> List[Image]:
    return image_repository.read_all()


def read_one_by_id(id: UUID) -> Image:
    return image_repository.read_one_by_id(id)


def create_one(entity: Image) -> Image:
    return image_repository.create_one(entity)


def patch_one_by_id(id, entity: Image) -> Image:
    return image_repository.patch_one_by_id(id, entity)


def delete_one_by_id(id) -> Image:
    return image_repository.delete_one_by_id(id)
