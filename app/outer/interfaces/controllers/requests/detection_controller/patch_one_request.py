from pydantic import BaseModel
from pydantic.types import UUID


class PatchOneRequest(BaseModel):
    image_id: UUID
    result: str
