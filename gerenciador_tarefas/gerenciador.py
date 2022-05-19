from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel, constr

# TAREFAS = [
#     {
#         "id": "1",
#         "titulo": "fazer compras",
#         "descrição": "comprar leite e ovos",
#         "estado": "não finalizado",
#     },
#     {
#         "id": "2",
#         "titulo": "levar o cachorro para tosar",
#         "descrição": "está muito peludo",
#         "estado": "não finalizado",
#     },
#     {
#         "id": "3",
#         "titulo": "lavar roupas",
#         "descrição": "estão sujas",
#         "estado": "não finalizado",
#     },
# ]

app = FastAPI()
class Tarefa(BaseModel):
    titulo: str

class Tarefa(BaseModel):
    titulo: constr(min_length=3, max_length=50)

TAREFAS = []


@app.get("/tarefas")
def listar():
    return TAREFAS

@app.post('/tarefas')
def criar():
    pass

@app.post('/tarefas')
def criar(tarefa: Tarefa):
    pass

