from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql import models
from sql.database import engine
from api.v1.api import api_router as api_router_v1

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="applabs_cadastro")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router_v1, prefix="/api/v1")

#https://github.com/plainspooky/utilizando-o-fastapi/blob/master/api/main.py
#TODO: Criar MicroServico Recurso
#TODO: Criar MicroServico pensar em algo