#Bibliotecas a importar
from fastapi import APIRouter,status,Response,HTTPException
from passlib.hash import sha256_crypt ##pa los usuarios (preguntar si horario == usuario)
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from datetime import datetime, timedelta
#imports de otros archivos
from config.db import con
from schemas.horario import horarioEntity, horariosEntity
from models.horario import Horario


#llamamos a la funcion para rutas de fastAPI y la almacenamos en horario pues estas seran las rutas relacionadas con esa coleccion
horario  = APIRouter()

#El endpoint para obtener todos horarios recordar que llamamos "horario" a las ocurrencias de un vehiculo detectado por las camaras 
@horario.get('/horarios')
async def find_all_horarios():
     return horariosEntity(con.test.horario.find())#Devolvemos un horariosEntity con todos los horarios en la base de datos

#Endpoint para obtener todos los horarios que tengan una licencia especifica en un timestamp de hace 30min hasta ahora
@horario.get('/horarios/30minuteTimeRange/{licence}/{timestamp}')
async def find_horarios_in_range(licence: str, timestamp: int):
    return horariosEntity(con.test.horario.find(
        {
            "licence": licence,
            "time" :{
                '$gte': (datetime.fromtimestamp(timestamp) - timedelta(minutes=300)),#buscamos un tiempo que sea hace 30min con el time delta
                '$lte': datetime.fromtimestamp(timestamp)
            }
        }
    ))

#endpoint para obtener todos los horarios dado un id
@horario.get('/horarios/{id}') 
async def find_horario(id: str):
    return horarioEntity(con.test.horario.find_one({"_id": ObjectId(id)})) #buscamos el horario con el id dado y lo retornamos 

#endpoint que obtiene los horarios dado un car_id   
@horario.get('/horarios/car_id/{id}')
async def find_horario(car_id: int):
    # Buscar el horario por el campo "car_id"
    horario_document = con.test.horario.find_one({"car_id": car_id})

    # Si no se encuentra el horario, devolver un error 404
    if horario_document is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado")

    # Crear la entidad de horario y devolverla
    return horarioEntity(horario_document)

#endpoint para ingresar un horario
@horario.post('/horarios')
async def create_horario(horario: Horario):
    new_horario = dict(horario)
    
    id = con.test.horario.insert_one(new_horario).inserted_id#insertamos el horario en la db y retornamos su id como confirmacion
    return str(id)


#endpoint para modificar un horario dado su id
@horario.put('/horarios/{car_id}')#
async def update_horario(car_id: int, horario: Horario):#solicitamos el id y el  nuevo horario
    con.test.horario.find_one_and_update({#usamos la funcion find_one_and_update para buscar un horario con el id dado y reemplazar sus datos por los nuevos
        "car_id": car_id
    }, {
        "$set": dict(horario)
    })
    return horarioEntity(con.test.horario.find_one({"car_id": car_id}))

#endpoint para eliminar un horario dado un id
@horario.delete('/horarios/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_horario(id: str):#solicitamos el id
    con.test.horario.find_one_and_delete({#usamos find_one_and_delete para borrar el objeto con ese id
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)

#endpoint para eliminar un horario dado un id
@horario.delete('/horarios/car_id/{car_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_horario(car_id: int):#solicitamos el car_id
    con.test.horario.find_one_and_delete({#usamos find_one_and_delete para borrar el objeto con ese id
        "car_id": car_id
    })
    return Response(status_code=HTTP_204_NO_CONTENT) 