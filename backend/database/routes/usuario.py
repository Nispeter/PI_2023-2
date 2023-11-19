from bson import ObjectId
from fastapi import APIRouter, status,Response
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from models.usuario import Usuario
from config.db import conn
from schemas.usuario import usuarioEntity, usuariosEntity

usuario = APIRouter()

@usuario.get('/usuarios', response_model=list[usuario], tags=["usuarios"])
async def find_all_usuarios():
    # print(list(conn.local.usuario.find()))
    return usuariosEntity(conn.local.usuario.find())


@usuario.post('/usuarios', response_model=usuario, tags=["usuarios"])
async def create_usuario(usuario: usuario):
    new_usuario = dict(usuario)
    new_usuario["password"] = sha256_crypt.encrypt(new_usuario["password"])
    del new_usuario["id"]
    id = conn.local.usuario.insert_one(new_usuario).inserted_id
    usuario = conn.local.usuario.find_one({"_id": id})
    return usuarioEntity(usuario)


@usuario.get('/usuarios/{id}', response_model=usuario, tags=["usuarios"])
async def find_usuario(id: str):
    return usuarioEntity(conn.local.usuario.find_one({"_id": ObjectId(id)}))


@usuario.put("/usuarios/{id}", response_model=usuario, tags=["usuarios"])
async def update_usuario(id: str, usuario: usuario):
    conn.local.usuario.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(usuario)
    })
    return usuarioEntity(conn.local.usuario.find_one({"_id": ObjectId(id)}))


@usuario.delete("/usuarios/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["usuarios"])
async def delete_usuario(id: str):
    conn.local.usuario.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)