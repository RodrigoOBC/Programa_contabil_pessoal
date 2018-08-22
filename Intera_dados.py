from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from banco_de_dados import getEngine, Gastos


def insert(valor,tp,data):

    gastos = Gastos(valor=valor,Tipo=tp,data_hora=data)

    DBSession = sessionmaker(bind=getEngine())
    session = DBSession()
    session.add(gastos)
    session.commit()

    return 'adcionado no BD'


def select(data):
    resultado = []
    DBSession = sessionmaker(bind=getEngine())
    session = DBSession()
    valores = session.query(Gastos).filter(Gastos.data_hora == data)
    valores = valores.all()
    for i in valores:
        resultado.append([i.valor,i.Tipo,i.data_hora])
    print(resultado)
    return resultado