from pydantic import BaseModel
from datetime import datetime
from typing import List
from models.auto import Auto
from models.lugar import Lugar
class Horario(BaseModel):
    car_id: int
    time: datetime
    lugar: dict[str, str] 
    licence: str
    probability: float
