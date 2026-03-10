from fastapi import FastAPI
from modelos import User

app = FastAPI()

usr = User(id=0, username="", email="")
users_list = []

@app.post("/setup")
async def setup(user: User):
    users_list.append(user)
    return {"message": "User created", "user": user}


@app.get("/")
async def root():
    return {"message": "a minha 1a fastapi"}

@app.get("/infos")
async def infos():
    return {"message": "Informações da minha fastapi"}

# criar 3 Endpoints estaticos

@app.get("/quote_motivacional")
async def quote():
    return {
        "quote": "O Fábio é incrível, lindo e maravilhoso.",
        "author": "Toda a gente que conhece o Fábio"
    }
    
@app.get("/config")
async def config():
    return {"version": "1.0"}

@app.get("/atec")
async def atec():
    return {"aluno": "Fábio", "curso": "Programação", "ano": 2023}

@app.get("/infos/{id}")
async def infos_detalhe(id: int):
    return {"message": f"Informações do ID: {id}"}

@app.get("/users")
async def users(pag: int = 1, num: int = 10):
    return {"message": "Lista de users",
            "pag": f"Página: {pag}",
            "user": f"User: {num}"}    
    
    
    
    
    
#3 endpoints com path param

@app.get("/produto/{id}")
async def produto(id: int):
    return {"produto_id": id}

@app.get("/aluno/{id}")
async def aluno(id: int):
    return {"aluno_id": id}

@app.get("/filme/{id}")
async def filme(id: int):
    return {"filme_id": id}


#3 endpoints com 1 query param 
@app.get("/pagina")
async def pagina(num: int):
    return {
        "pagina": num
    }

@app.get("/categoria")
async def categoria(tipo: str):
    return {
        "categoria": tipo
    }

@app.get("/jogo")
async def jogo(nome: str):
    return {
        "jogo": nome
    }
#3 endpoints com mais de 1 query param

@app.get("/produtos")
async def produtos(nome: str, preco: int):
    return {"produto": nome, "preco": preco}  

@app.get("/filmes")
async def filmes(genero: str, ano: int):
    return {
        "genero": genero,
        "ano": ano
    }  

@app.get("/cursos")
async def cursos(nome: str, nivel: int):
    return {
        "curso": nome,
        "nivel": nivel
    }
    
    
    
    
@app.get("/addUser") # nao mexer
async def user(id:int, nome:str, email:str): # nao mexer
    new_usr = User(id=id, username=nome, email=email)
    return {"msg": f"User {new_usr.username} criado"}