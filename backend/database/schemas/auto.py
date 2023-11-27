def autoEntity(item) -> dict:
    # Convierte un elemento de la base de datos (item) a un diccionario con un formato especifico
    return {
        "id": str(item["_id"]),        # Convierte el ObjectId a una cadena
        "patente": item["patente"],    # Obtiene la patente del auto
        "modelo": item["modelo"],      # Obtiene el modelo del auto
        "ano": item["ano"],            # Obtiene el año del auto
        "propietario": item["propietario"]  # Obtiene la información del propietario del auto
    }

def autosEntity(entity) -> list:
    # Convierte una lista de elementos de la base de datos a una lista de diccionarios
    # utilizando la función autoEntity para cada elemento
    return [autoEntity(item) for item in entity]
