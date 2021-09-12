from .base import CRUDBase
from sql import models
from schemas import processo

class CRUDProcesso(CRUDBase[models.Processo, processo.ProcessoCreate, processo.ProcessoUpdate]):
    pass


processo = CRUDProcesso(models.Processo)