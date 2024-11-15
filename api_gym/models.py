from sqlalchemy import Column, Integer, String
from .database import Base

class Exercicio(Base):
    __tablename__ = "exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    url_video = Column(String)
    descricao = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
<<<<<<< HEAD
    hashed_password = Column(String)
=======
    hashed_password = Column(String)
>>>>>>> 8e13545a7acce39a6482b755a0a67e23967415f9
