from pydantic.types import UUID, List

from app.core.models.entities.Detection import Detection
from app.outer.repositories import detection_repository


def read_all() -> List[Detection]:
    return detection_repository.read_all()


def read_one_by_id(id: UUID) -> Detection:
    return detection_repository.read_one_by_id(id)


def create_one(entity: Detection) -> Detection:
    return detection_repository.create_one(entity)


def patch_one_by_id(id, entity: Detection) -> Detection:
    return detection_repository.patch_one_by_id(id, entity)


def delete_one_by_id(id) -> Detection:
    return detection_repository.delete_one_by_id(id)
