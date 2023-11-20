from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[str] = None
    nombre: str
    correo: str
    password: str

