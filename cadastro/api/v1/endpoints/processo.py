from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import processo as schema_processo
from tasks.filas import publish
from sql.database import get_db
import json

from crud.processo import processo as crudProcesso

router = APIRouter()

@router.post("/processos/", status_code=status.HTTP_201_CREATED)
async def create_processo(processo: schema_processo.ProcessoCreate, db: Session = Depends(get_db)):    
    result = crudProcesso.create(db, obj_in=processo)
    publish(fila='create_recurso', p_exchange='recurso', msg=json.dumps({"processo_id":result.id, "nome_processo":result.nome, "servidor":result.servidor, "sistema":result.sistema}))
    return result

@router.get("/processos/",  status_code=status.HTTP_200_OK)
async def processos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    processos = crudProcesso.get_multi(db,skip=skip, limit=limit)
    return processos

@router.get("/processos/{id}/", status_code=status.HTTP_200_OK)
async def processo(id: int, db: Session = Depends(get_db)):
    if db_processo := crudProcesso.get(db, id):
        return db_processo
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Processo id={id} não encontrado.",
    )

@router.delete("/processos/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def processo(id: int, db: Session = Depends(get_db)):    
    if not crudProcesso.delete(db, id=id):
    #if not crud.delete_processo(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Processo de 'id={id}' não encontrado.",
        )

@router.put("/processos/{id}/", status_code=status.HTTP_201_CREATED)
def update_processo(
    *,
    db: Session = Depends(get_db),
    id: int,
    processo_in: schema_processo.ProcessoUpdate,
):

    processo = crudProcesso.get(db, id=id)
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Processo id={id} não encontrado.",
        )
    return crudProcesso.update(db, db_obj=processo, obj_in=processo_in)

#https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/api/api_v1/endpoints/users.py