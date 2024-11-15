from sqlalchemy.orm import Session
from .models import Exercicio
from .schemas import ExercicioCriar


# Função para criar um exercício
def criar_exercicio(db: Session, exercicio: ExercicioCriar):
    db_exercicio = Exercicio(**exercicio.model_dump())
    db.add(db_exercicio)
    db.commit()
    db.refresh(db_exercicio)
    return db_exercicio

# exercício pelo ID
def obter_exercicio_por_id(db: Session, exercicio_id: int):
    return db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()

#get pelo ID
def obter_exercicio(db: Session, exercicio_id: int):
    return obter_exercicio_por_id(db, exercicio_id)

#get
def obter_exercicios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Exercicio).offset(skip).limit(limit).all()

#put
def atualizar_exercicio(db: Session, exercicio_id: int, dados_exercicio: ExercicioCriar):
    db_exercicio = obter_exercicio_por_id(db, exercicio_id)
    if db_exercicio:
        db_exercicio.nome = dados_exercicio.nome
        db_exercicio.url_video = dados_exercicio.url_video
        db_exercicio.descricao = dados_exercicio.descricao
        db.commit()
        db.refresh(db_exercicio)
        return db_exercicio
    return None

# delete
def deletar_exercicio(db: Session, exercicio_id: int):
    db_exercicio = obter_exercicio_por_id(db, exercicio_id)
    if db_exercicio:
        db.delete(db_exercicio)
        db.commit()
        return {"mensagem": "Exercicio deletado"}
    return {"mensagem": "Exercicio não encontrado"}
