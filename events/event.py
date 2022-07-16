from typing import Optional, Any, List

from pydantic import BaseModel


class EventProperties(BaseModel):
    target_objects: List[str]
    value: str | int


class Event(BaseModel):
    id: Optional[int] = None
    name: str
    type: str = "event"
    properties: EventProperties
    addittional_properties: dict = {}
    active: bool = True
    action: Any
