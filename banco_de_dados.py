mport datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Gastos(Base):
    __tablename__ = 'gastos'
    id_gastos = Column(Integer,primary_key=True,autoincrement=True)
    valor = Column(Float,nullable=False)
    Tipo = Column(String,nullable=False)
    data_hora = Column(String,nullable=False)

def getEngine():
    engine = create_engine('caminho do seu banco de dados')
    return engine

def criar_bd():
    Base.metadata.create_all(getEngine())