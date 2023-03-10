from datetime import datetime

from pydantic import BaseModel
from pydantic.types import UUID
from sqlmodel import SQLModel, Field


class Recognition(SQLModel, table=True):
    __tablename__: str = "recognition"
    id: UUID = Field(primary_key=True)
    image_id: UUID = Field(foreign_key="image.id")
    result: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
