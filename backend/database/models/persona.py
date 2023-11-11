from pydantic import BaseModel
from typing import Optional

class Persona(BaseModel):
    id: Optional[str] = None
    rut: str
    nombre: str
    rol: str

