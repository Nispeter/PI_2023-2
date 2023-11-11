def usuarioEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "correo": (item["correo"]),
        "nombre": item["nombre"],
        "password": item["password"]
    }
def usuariosEntity(entity) -> list:
    return [usuarioEntity(item) for item in entity]