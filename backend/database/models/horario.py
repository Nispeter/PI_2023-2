from pydantic import BaseModel
from typing import List
from models.auto import Auto
from models.lugar import Lugar
class Horario(BaseModel):
    hora: int
    minuto: int
    segundo: int
    lugar: dict[str, str] 
    auto: dict
    confianza: float
