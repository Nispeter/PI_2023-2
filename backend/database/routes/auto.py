from fastapi import APIRouter,status,Response
from passlib.hash import sha256_crypt ##pa los usuarios (preguntar si auto == usuario)
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
import json 
from config.db import con
from schemas.auto import autoEntity, autosEntity
from models.auto import Auto
from models.persona import Persona
from schemas.persona import personaEntity, personasEntity


auto = APIRouter()

@auto.get('/autos')
async def find_all_autos():
     return autosEntity(con.test.auto.find())

@auto.get('/autos/{id}')
async def find_auto(id: str):
    return autoEntity(con.test.auto.find_one({"_id": ObjectId(id)}))
    

@auto.post('/autos')
async def create_auto(auto: Auto):
    rut_propietario = auto.propietario["rut"]
    persona_data = con.test.persona.find_one({"rut": rut_propietario})
    
    print("Tipo de persona_data:", type(persona_data))
    print("persona_data:", persona_data)

    if not persona_data:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")

    # Crear un objeto Persona directamente con los datos necesarios
    propietario = Persona(
        id=str(persona_data["_id"]),  # Convertir el ObjectId a una cadena
        rut=persona_data["rut"],
        nombre=persona_data["nombre"],
        rol=persona_data["rol"]
    )

    # Convertir el objeto Persona a un diccionario usando el método dict() de Pydantic
    propietario_dict = propietario.dict()
    
    new_auto = {
        "patente": auto.patente,
        "modelo": auto.modelo,
        "año": auto.año,
        "propietario": propietario_dict
    }
    print("propietario: ", new_auto["propietario"])
    auto_id = con.test.auto.insert_one(new_auto).inserted_id

    return autoEntity(con.test.auto.find_one({"_id": ObjectId(auto_id)}))



@auto.put('/autos/{id}')
async def update_auto(id: str, auto: Auto):
    con.test.auto.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(auto)
    })
    return autoEntity(con.test.auto.find_one({"_id": ObjectId(id)}))

@auto.delete('/autos/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_auto(id: str):
    con.test.auto.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)
    