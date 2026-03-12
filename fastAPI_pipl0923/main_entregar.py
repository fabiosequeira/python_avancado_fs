from fastapi import FastAPI, HTTPException
from modelos import User

app = FastAPI()

usr = User(id=0, username="", email="")
users_list = []


@app.post("/adduser", status_code=201)
async def setup(user: User):
    # TODO:  adicionar alunos a uma lista de alunos
    for u in users_list:
        if u.id == user.id:
            return HTTPException(status_code=400, detail="User com este ID já existe")
    users_list.append(user)
    return {"Adicionado": user}

@app.get("/users")
async def users():
    # TODO: Mostrar todos os alunos
    return {
        "msg": "Lista de utilizadores",
        "users": users_list
    }

@app.get("/users/{id}")
async def user_by_id(id: int):
    # TODO:  Mostrar o aluno com o id indicado
    for user in users_list:
        if user.id == id:
            return user

    return {"erro": "User não encontrado"}
