#Bibliotecas a importar
from fastapi import APIRouter,status,Response
from passlib.hash import sha256_crypt ##pa los usuarios (preguntar si auto == usuario)
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
import json 
#Importamos desde otros archivos del proyecto
from config.db import con
from schemas.auto import autoEntity, autosEntity
from models.auto import Auto
from models.persona import Persona
from schemas.persona import personaEntity, personasEntity

#llamamos a la funcion para rutas de fastAPI y la almacenamos en auto pues estas seran las rutas relacionadas con esa coleccion
auto = APIRouter()
#El endpoint para obtener todos los autos
@auto.get('/autos')
async def find_all_autos():
     return autosEntity(con.test.auto.find())#retornamos una autosEntity con el resultlado de encontrar todos los autos


#enpoint para obtener un auto dado un id 
@auto.get('/autos/{id}')#pedimos el id
async def find_auto(id: str):
    return autoEntity(con.test.auto.find_one({"_id": ObjectId(id)}))#retornamos un autoEntity con el resultado de la query de buscar un auto dado un ID

#enpoint para obtener un auto dado una patente
@auto.get('/autos/patente/{patente}')
async def find_auto(patente: str):#pedimos la patente
    return autoEntity(con.test.auto.find_one({"patente": patente}))#retornamos un autoEntity con el resultado de la query de buscar un auto dado una patente
    

#endpoint para ingresar un auto a la base de datos
@auto.post('/autos')
async def create_auto(auto: Auto):#pedimos el objeto auto
    #pasamos el auto a dict()
    new_auto = dict(auto)
    
    #Creamos el auto con la informacion dada
    auto_id = con.test.auto.insert_one(new_auto).inserted_id

    #retornamos el id a modo de confirmacion
    return autoEntity(con.test.auto.find_one({"_id": ObjectId(auto_id)}))


#endpoint para modificar un auto dado su id
@auto.put('/autos/{id}')
async def update_auto(id: str, auto: Auto): #solicitamos el id y el nuevo contenido
    con.test.auto.find_one_and_update({#llamamos al metodo find_one_and_update para encontrar un auto con el id dado y reemplazar sus datos por los ingresados
        "_id": ObjectId(id)
    }, {
        "$set": dict(auto)
    })
    return autoEntity(con.test.auto.find_one({"_id": ObjectId(id)}))#retornamos el id del auto a modo de confirmacion

#endpoint para eliminar un auto
@auto.delete('/autos/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_auto(id: str):#pedimos un id
    con.test.auto.find_one_and_delete({#llamamos a la funcion find_one_and_delete para buscar y eliminar el auto con el id dado
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)#retornamos una respuesta http
    
#endpoint para obtener todas las patentes de los autos ingresados    
@auto.get('/autos_plates')
async def get_plates():
    autos_documents = con.test.auto.find()#hacemos un find de todos los autos
    autos_list = autosEntity(autos_documents)#los convertimos en una autosEntity
    plates = [auto["patente"] for auto in autos_list]#extraemos de ahi las patentes
    return plates#las retornamos
