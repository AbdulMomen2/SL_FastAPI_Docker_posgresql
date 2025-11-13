from pydantic import BaseModel
from typing import List


class EventSchema(BaseModel):
    id: int

class EventListSchema(BaseModel):
    results: List[EventSchema]

class BookSchema(BaseModel):
    id: int   
    name: str
    category: List[str]
