def autoEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "patente": item["patente"],
        "modelo": item["modelo"],
        "año": item["año"],
        "propietario": item["propietario"]
    }
def autosEntity(entity) -> list:
    return [autoEntity(item) for item in entity]