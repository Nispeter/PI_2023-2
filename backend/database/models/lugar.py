from pydantic import BaseModel
from typing import List

class Lugar(BaseModel): 
    latitud: str
    longitud: str
