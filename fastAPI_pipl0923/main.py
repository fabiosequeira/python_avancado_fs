from fastapi import FastAPI, HTTPException
from modelos import User

app = FastAPI()

usr = User(id=0, username="", email="")
users_list = [User(id=1, username="fabio", email="fabio@email.com"),
    User(id=2, username="bianca", email="bianca@email.com"),
    User(id=3, username="angie", email="angie@email.com"),
    User(id=4, username="bruna", email="bruna@email.com"),
    User(id=5, username="erica", email="erica@email.com")]




# @app.get("/")
# async def root():
#     return {"message": "a minha 1a fastapi"}

# @app.get("/infos")
# async def infos():
#     return {"message": "Informações da minha fastapi"}

# # criar 3 Endpoints estaticos

# @app.get("/quote_motivacional")
# async def quote():
#     return {
#         "quote": "O Fábio é incrível, lindo e maravilhoso.",
#         "author": "Toda a gente que conhece o Fábio"
#     }
    
# @app.get("/config")
# async def config():
#     return {"version": "1.0"}

# @app.get("/atec")
# async def atec():
#     return {"aluno": "Fábio", "curso": "Programação", "ano": 2023}

# @app.get("/infos/{id}")
# async def infos_detalhe(id: int):
#     return {"message": f"Informações do ID: {id}"}


    
    
    
    
    
# #3 endpoints com path param

# @app.get("/produto/{id}")
# async def produto(id: int):
#     return {"produto_id": id}

# @app.get("/aluno/{id}")
# async def aluno(id: int):
#     return {"aluno_id": id}

# @app.get("/filme/{id}")
# async def filme(id: int):
#     return {"filme_id": id}


# #3 endpoints com 1 query param 
# @app.get("/pagina")   
# async def pagina(num: int):
#     return {
#         "pagina": num
#     }

# @app.get("/categoria")
# async def categoria(tipo: str):
#     return {
#         "categoria": tipo
#     }

# @app.get("/jogo")
# async def jogo(nome: str):
#     return {
#         "jogo": nome
#     }
# #3 endpoints com mais de 1 query param

# @app.get("/produtos")
# async def produtos(nome: str, preco: int):
#     return {"produto": nome, "preco": preco}  

# @app.get("/filmes")
# async def filmes(genero: str, ano: int):
#     return {
#         "genero": genero,
#         "ano": ano
#     }  

# @app.get("/cursos")
# async def cursos(nome: str, nivel: int):
#     return {
#         "curso": nome,
#         "nivel": nivel
#     }
    
    
    
    
# @app.get("/addUser") # nao mexer
# async def user(id:int, nome:str, email:str): # nao mexer
#     new_usr = User(id=id, username=nome, email=email)
#     return {"msg": f"User {new_usr.username} criado"}




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

