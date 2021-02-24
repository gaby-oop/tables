import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    password = Column(String(200))
   
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    estatura = Column(String(200))
    birthyear= Column(String(200), nullable=False)
    gender= Column(String(200))

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    size = Column(String(200))
    diametro = Column(String(200), nullable=False)
    gravedad = Column(String(200))

class favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    personajes_id  = Column(Integer, ForeignKey ("personajes.id"))
    planetas_id  = Column(Integer, ForeignKey ("planetas.id"))
    usuario_id  = Column(Integer, ForeignKey ("usuario.id"))
    def to_dict(self):
        return {}
render_er(Base, 'diagram.png')

## Draw from SQLAlchemy base