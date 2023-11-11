from pydantic import BaseModel
from typing import List
from models.persona import Persona
class Auto(BaseModel):
    patente: str
    modelo: str
    año: int
    propietario: List[str]
