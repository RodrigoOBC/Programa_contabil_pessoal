import sqlite3
from banco_de_dados import Recebimento
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

NOME = 'gastos.db'
NOME_TABLE = Recebimento.__tablename__

conn = sqlite3.connect(rf'caminho do sue banco de dados')
c = conn.cursor()

def inserir(valores):
    c.execute(f"INSERT INTO {NOME_TABLE} VALUES {valores}")
    conn.commit()