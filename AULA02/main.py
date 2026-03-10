from modelos import Carro, Livro, Pessoa

# c4 = Carro(marca="Citroen", modelo="C4", ano=2008, num_km=226000.0, tanque_litros=50.0)
# print(f"O meu carro e um ",c4.marca, c4.modelo," de ",c4.ano," com ",c4.num_km," km rodados.")

# l1 = Livro(titulo="The Three-Body Problem", autor="Cixin Liu", ano=2015, editora="Head of Zeus", num_paginas=416, genero="Ficção Cientifica", classificacao_etaria=16, rating=4.5)
# print(f"O livro '{l1.titulo}' foi escrito por {l1.autor} e publicado em {l1.ano} pela editora {l1.editora}.")




# c4.andar(100, 120, 45.0)  # 200 km

# print(f"{c4.calcular_consumo():.2f} L/100km")


p1 = Pessoa(nome="Ana Clara", idade=22, altura=1.65, peso=60000.0, energia=100)
p1.comer(["maçã", "banana", "picanha"])
p1.falar()

print(p1.peso)