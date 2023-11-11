from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from models.persona import Persona
# from models.Rol import Rol
# from models.Auto import Auto
from controllers.Persona import app as personas_app

app = FastAPI()

# Configura la conexión a la base de datos MongoDB
uri = "mongodb+srv://jeesus1423:9OvLdYJuR2DjhU7O@cluster0.oirouk8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

# Ruta para verificar la conexión a la base de datos
@app.get("/ping_mongodb")
def ping_mongodb():
    try:
        client.admin.command('ping')
        return {"message": "Pinged your MongoDB deployment. You successfully connected to MongoDB!"}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}

# Define tus otras rutas y lógica de negocio aquí
app.mount("/personas", personas_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
