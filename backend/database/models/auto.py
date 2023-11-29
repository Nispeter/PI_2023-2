#imports de bibliotecas
from pydantic import BaseModel, Field
from typing import List

#imports de otros archivos del proyecto
from models.persona import Persona

class Auto(BaseModel):
    # Definición de los campos del modelo Auto

    # Campo para la patente del auto
    patente: str

    # Campo para el modelo del auto
    modelo: str

    # Campo para el año del auto
    ano: int

    # Campo para el rut del propietario del auto, esto sera para buscar el resto de informacion del propietario en el post
    rut: str
