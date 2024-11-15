from pydantic import BaseModel

class ExercicioCriar(BaseModel):
    nome: str
    url_video: str
    descricao: str

class ExercicioResposta(BaseModel):
    id: int
    nome: str
    url_video: str
    descricao: str

    class Config:
        orm_mode = True