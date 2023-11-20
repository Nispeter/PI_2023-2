from pymongo import MongoClient
from fastapi import FastAPI
from models.Persona import Persona


# Crea una instancia de FastAPI
app = FastAPI()

# Conecta a la base de datos MongoDB utilizando la URI
uri = "mongodb+srv://jeesus1423:M6OMRQL4YT4PtVdO@cluster0.oirouk8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

# Selecciona la base de datos
db = client.nombre_de_tu_base_de_datos  # Reemplaza "nombre_de_tu_base_de_datos" con el nombre de tu base de datos

# Selecciona la colección de personas
personas_collection = db.personas  # Reemplaza "personas" con el nombre de tu colección de personas

# Define una ruta para agregar una nueva persona
@app.get("/personas/")
async def create_persona(persona: Persona):
    try:
        # Convierte el objeto Persona de Pydantic a un diccionario de Python
        persona_data = persona.dict()

        # Inserta la persona en la colección de personas
        personas_collection.insert_one(persona_data)

        # Devuelve una respuesta indicando que la persona ha sido creada exitosamente
        return {"message": "Persona creada exitosamente"}
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir durante la inserción
        return {"error": str(e)}
