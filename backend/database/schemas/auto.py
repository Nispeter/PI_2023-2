def autoEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "patente": item["patente"],
        "modelo": item["modelo"],
        "año": item["año"],
<<<<<<< HEAD
        "propietario": item["propietario"]
=======
        "propietario": [str(owner_id) for owner_id in item.get("propietario", [])]
>>>>>>> dev
    }
def autosEntity(entity) -> list:
    return [autoEntity(item) for item in entity]