from pydantic import BaseModel, Field
from typing import List
from models.persona import Persona
class Auto(BaseModel):
    patente: str
    modelo: str
    año: int
    propietario: dict = Field(..., alias="propietario")
