import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
# se crea  la tabla del usuario
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(50), nullable=False)
# creacion de la tabla correspondiente character
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(Integer, ForeignKey('person.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Planetas(Base):
    __tablename__='planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    terrain = Column(String(50))
    user = relationship(User)

class Vehiculos(Base):
    __tablename__='vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(50), nullable=False)
    passengers = Column(Integer)
    cost = Column(Integer)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
