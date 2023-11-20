def horarioEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "car_id": item["car_id"],
        "time": item["time"],
        "lugar": item["lugar"],
        "licence": item["licence"],
        "probability": item["probability"]
    }
def horariosEntity(entity) -> list:
    return [horarioEntity(item) for item in entity]