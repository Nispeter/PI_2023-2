from fastapi import FastAPI
from routes.persona import persona 
from routes.auto import auto
from routes.horario import horario
app = FastAPI()

app.include_router(horario)
app.include_router(persona)
app.include_router(auto)

