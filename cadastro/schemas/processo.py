from pydantic import BaseModel, validator
from typing import Optional

class ProcessoBase(BaseModel):
    nome: str
    job: str
    sistema: str
    servidor: str
    path: str

    @validator("nome")
    def validate_nome(cls, v: str, **kwargs: int) -> str:
        if len(v) < 5:
            raise ValueError("Minimo 5 caracteres para nome !")
        return v  

class ProcessoCreate(ProcessoBase):
    pass

class ProcessoUpdate(ProcessoBase):
    pass

class Processo(ProcessoBase):
    id: int
    class Config:
        orm_mode = True