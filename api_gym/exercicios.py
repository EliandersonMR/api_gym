from sqlalchemy.orm import Session
from api_gym.models import Exercicio
from api_gym.schemas import ExercicioCriar

def criar_exercicios_iniciais(db: Session, exercicios: list):
    for exercicio in exercicios:
        db_exercicio = Exercicio(**exercicio)
        db.add(db_exercicio)
    db.commit()

def criar_exercicio(db: Session, exercicio: ExercicioCriar):
    db_exercicio = Exercicio(**exercicio.dict())
    db.add(db_exercicio)
    db.commit()
    db.refresh(db_exercicio)
    return db_exercicio

def obter_exercicio(db: Session, exercicio_id: int):
    return db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()

def obter_exercicios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Exercicio).offset(skip).limit(limit).all()

def atualizar_exercicio(db: Session, exercicio_id: int, exercicio: ExercicioCriar):
    db_exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
    if db_exercicio:
        for key, value in exercicio.dict().items():
            setattr(db_exercicio, key, value)
        db.commit()
        db.refresh(db_exercicio)
    return db_exercicio

def deletar_exercicio(db: Session, exercicio_id: int):
    db_exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
    if db_exercicio:
        db.delete(db_exercicio)
        db.commit()
    return db_exercicio
