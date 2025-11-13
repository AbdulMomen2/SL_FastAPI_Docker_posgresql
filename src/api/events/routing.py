from fastapi import APIRouter
from .schema import EventSchema, EventListSchema, BookSchema

import json

router = APIRouter()

# Best approach:
@router.get("/")
def read_events() -> EventListSchema:
    # Create proper EventSchema objects
    events = [EventSchema(id=i) for i in [1, 2, 3]]
    return EventListSchema(results=events)

#single item
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id)


#POST/api/events
@router.post("/")
def create_event(data: dict) -> EventSchema:
    print(type(data))
    return EventSchema(id=123)

@router.post("/books", response_model=BookSchema)
def create_book(data: BookSchema)-> BookSchema:
    return data