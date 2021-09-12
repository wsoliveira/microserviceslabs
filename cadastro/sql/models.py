from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from .database import Base

class Processo(Base):
    __tablename__ = "processos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)
    job = Column(String, index=True)
    sistema = Column(String, index=True)
    servidor = Column(String, index=True)
    path = Column(String, default=None, nullable=False)