from fastapi import APIRouter,status,Response
from passlib.hash import sha256_crypt ##pa los usuarios (preguntar si horario == usuario)
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from config.db import con
from schemas.horario import horarioEntity, horariosEntity
from models.horario import Horario


horario = APIRouter()

@horario.get('/horarios')
async def find_all_horarios():
     return horariosEntity(con.test.horario.find())

@horario.get('/horarios/{id}')
async def find_horario(id: str):
    return horarioEntity(con.test.horario.find_one({"_id": ObjectId(id)}))
    

@horario.post('/horarios')
async def create_horario(horario: Horario):
    new_horario = dict(horario)
    # Convierte el campo 'lugar' en un diccionario
    new_horario['lugar'] = dict(horario.lugar)
    
    id = con.test.horario.insert_one(new_horario).inserted_id
    return str(id)

@horario.put('/horarios/{id}')
async def update_horario(id: str, horario: Horario):
    con.test.horario.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(horario)
    })
    return horarioEntity(con.test.horario.find_one({"_id": ObjectId(id)}))

@horario.delete('/horarios/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_horario(id: str):
    con.test.horario.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)
    