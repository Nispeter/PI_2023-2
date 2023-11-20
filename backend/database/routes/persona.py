from fastapi import APIRouter,status,Response
from passlib.hash import sha256_crypt ##pa los usuarios (preguntar si persona == usuario)
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from config.db import con
from schemas.persona import personaEntity, personasEntity
from models.persona import Persona


persona = APIRouter()

@persona.get('/personas')
async def find_all_personas():
     return personasEntity(con.test.persona.find())

@persona.get('/personas/{id}')
async def find_persona(id: str):
    return personaEntity(con.test.persona.find_one({"_id": ObjectId(id)}))
<<<<<<< HEAD

@persona.get('/personas/rut/{rut}')
async def find_persona(rut: str):
    return personaEntity(con.test.persona.find_one({"rut": rut}))
       
=======
    
>>>>>>> dev

@persona.post('/personas')
async def create_persona(persona: Persona):
    new_persona = dict(persona)
    del new_persona["id"]
    id = con.test.persona.insert_one(new_persona).inserted_id
    return str(id)

@persona.put('/personas/{id}')
async def update_persona(id: str, persona: Persona):
    con.test.persona.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(persona)
    })
    return personaEntity(con.test.persona.find_one({"_id": ObjectId(id)}))

@persona.delete('/personas/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_persona(id: str):
    con.test.persona.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)
    