from fastapi import FastAPI
from routes.persona import persona 
from routes.auto import auto
from routes.horario import horario
<<<<<<< HEAD
from fastapi.middleware.cors import CORSMiddleware

=======
>>>>>>> dev
app = FastAPI()

app.include_router(horario)
app.include_router(persona)
app.include_router(auto)

<<<<<<< HEAD
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
=======
>>>>>>> dev
