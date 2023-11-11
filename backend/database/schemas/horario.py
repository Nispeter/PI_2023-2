def horarioEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "hora": item["hora"],
        "minuto": item["minuto"],
        "segundo": item["segundo"],
        "lugar": item["lugar"],
        "auto": item["auto"],
        "confianza": item["confianza"]
    }
def horariosEntity(entity) -> list:
    return [horarioEntity(item) for item in entity]