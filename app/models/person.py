from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    age: int
