from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api_gym.auth import criar_token, verificar_credenciais
from api_gym.database import SessionLocal, engine
from api_gym.models import Base, User
from api_gym.schemas import ExercicioCriar, ExercicioResposta
from api_gym.exercicios import (
    criar_exercicio,
    obter_exercicio,
    obter_exercicios,
    atualizar_exercicio,
    deletar_exercicio
)

# Banco de dados
Base.metadata.create_all(bind=engine)

# Sessão do banco de dados
def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verificar_credenciais(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Nome de usuário ou senha incorretos"
        )
    token_data = {"sub": user["username"]}
    token = criar_token(token_data)
    return {"access_token": token, "token_type": "bearer"}


# Endpoints de CRUD de exercícios, protegidos pelo token
@app.post("/exercicios/", response_model=ExercicioResposta)
async def criar_exercicio_endpoint(exercicio: ExercicioCriar, db: Session = Depends(obter_db), token: str = Depends(verificar_credenciais)):
    return criar_exercicio(db, exercicio)

@app.get("/exercicios/{exercicio_id}", response_model=ExercicioResposta)
async def obter_exercicio_endpoint(exercicio_id: int, db: Session = Depends(obter_db), token: str = Depends(verificar_credenciais)):
    db_exercicio = obter_exercicio(db, exercicio_id)
    if db_exercicio is None:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio

@app.get("/exercicios/", response_model=list[ExercicioResposta])
async def obter_exercicios_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(obter_db), token: str = Depends(verificar_credenciais)):
    db_exercicio = obter_exercicios(db, skip=skip, limit=limit)
    return db_exercicio

@app.put("/exercicios/", response_model=ExercicioResposta)
async def atualizar_exercicio_endpoint(exercicio_id: int, exercicio: ExercicioCriar, db: Session = Depends(obter_db), token: str = Depends(verificar_credenciais)):
    db_exercicio = atualizar_exercicio(db, exercicio_id, exercicio)
    if db_exercicio is None:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio

@app.delete("/exercicios/{exercicio_id}", response_model=ExercicioResposta)
async def deletar_exercicio_endpoint(exercicio_id: int, db: Session = Depends(obter_db), token: str = Depends(verificar_credenciais)):
    db_exercicio = deletar_exercicio(db, exercicio_id)
    if db_exercicio is None:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio


origins = [
    "http://localhost",  
    "http://127.0.0.1", 
    "http://192.168.1.104",
    "http://localhost:5500",
    "http://localhost:8080",  
    "https://api-gym-1.onrender.com",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)
