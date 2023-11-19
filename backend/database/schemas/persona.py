def personaEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "rut": item["rut"],
        "nombre": item["nombre"],
        "rol": item["rol"]
    }
def personasEntity(entity) -> list:
    return [personaEntity(item) for item in entity]