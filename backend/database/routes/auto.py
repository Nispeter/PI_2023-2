from fastapi import APIRouter,status,Response
from passlib.hash import sha256_crypt ##pa los usuarios (preguntar si auto == usuario)
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from config.db import con
from schemas.auto import autoEntity, autosEntity
from models.auto import Auto


auto = APIRouter()

@auto.get('/autos')
async def find_all_autos():
     return autosEntity(con.test.auto.find())

@auto.get('/autos/{id}')
async def find_auto(id: str):
    return autoEntity(con.test.auto.find_one({"_id": ObjectId(id)}))
    

@auto.post('/autos')
async def create_auto(auto: Auto):
    new_auto = dict(auto)
    
    id = con.test.auto.insert_one(new_auto).inserted_id
    return str(id)

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
    
#@auto.get('/autos/check_plate/{license_plate}')
async def check_license_plate(license_plate: str):
    auto_document = con.test.auto.find_one({"patente": license_plate})
    if auto_document:
        return {"status": "found", "auto": autoEntity(auto_document)}
    else:
        handle_license_plate_not_found(license_plate)
        return {"status": "not found"}


def handle_license_plate_not_found(license_plate: str):
    print(":(")
    #Check  time or smt