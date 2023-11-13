from fastapi import APIRouter,status,Response,HTTPException
from passlib.hash import sha256_crypt ##pa los usuarios (preguntar si horario == usuario)
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from datetime import datetime, timedelta

from config.db import con
from schemas.horario import horarioEntity, horariosEntity
from models.horario import Horario


horario = APIRouter()

@horario.get('/horarios')
async def find_all_horarios():
     return horariosEntity(con.test.horario.find())

@horario.get('/horarios/30minuteTimeRange/{licence}/{timestamp}')
async def find_horarios_in_range(licence: str, timestamp: int):
    return horariosEntity(con.test.horario.find(
        {
            "licence": licence,
            "time" :{
                '$gte': (datetime.fromtimestamp(timestamp) - timedelta(minutes=40)),
                '$lte': datetime.fromtimestamp(timestamp)
            }
        }
    ))

@horario.get('/horarios/{id}') 
async def find_horario(id: str):
    return horarioEntity(con.test.horario.find_one({"_id": ObjectId(id)}))
    
@horario.get('/horarios/car_id/{id}')
async def find_horario(car_id: int):
    # Buscar el horario por el campo "car_id"
    horario_document = con.test.horario.find_one({"car_id": car_id})

    # Si no se encuentra el horario, devolver un error 404
    if horario_document is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado")

    # Crear la entidad de horario y devolverla
    return horarioEntity(horario_document)

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
    