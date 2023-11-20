<<<<<<< HEAD
from pydantic import BaseModel, Field
=======
from pydantic import BaseModel
>>>>>>> dev
from typing import List
from models.persona import Persona
class Auto(BaseModel):
    patente: str
    modelo: str
    año: int
<<<<<<< HEAD
    rut: str
=======
    propietario: List[str]
>>>>>>> dev
