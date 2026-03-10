# nome = "Fabio"
# ano = 2026

# print("Ola " + nome + " em " + str(ano))
# print (f"Ola {nome} em {ano}")
# print ("Ola", nome , "em", ano)

# n1 = 10
# n2 = 10.0

# soma = n1 + n2
# sub = n1 - n2
# multi = n1 * n2
# div = n1 / n2
# print(soma)
# print(sub)
# print(multi)
# print(div)






































# idade = int(input("Introduz a idade: "))

# if idade <= 12:
#     print("A pessoa e uma criança.")
# elif idade < 18:
#     print("A pessoa e um adolescente.")
# else:
#     print("A pessoa e um adulto.")





#crie uma app que recveba 2 notas

# se as duas notas forem positivas (mais de 10) o aluno esta aprovado
# se apenas uma das notas for positiva pode fazer recuperação
# se as duas notas forem negativas o aluno esta reprovado


# nota1 = float(input("Introduz a primeira nota: "))
# nota2 = float(input("Introduz a segunda nota: "))

# if nota1 >= 10 and nota2 >= 10:
#     print("Aluno aprovado")
# elif nota1 >= 10 or nota2 >= 10:
#     print("Aluno pode fazer recuperação")
# else:
#     print("Aluno reprovado")



# crie um menu com 3 opcoes
#  na opt1 mostre a msg "ola mundo"
#  na opt2 mostre a msg "bom dia"
#  na opt3 mostre a msg "boa noite"
#  se a opt for invalida indique a opt e invalida

# print("Menu: ")
# print("Opção 1")
# print("Opção 2")
# print("Opção 3")
# opt = input("Escolha uma opcao: ")

# match opt:
#     case "1":
#         print("Ola Mundo")
#     case "2":
#         print("Bom Dia")
#     case "3":
#         print("Boa Noite")
#     case _:
#         print("Opcao invalida")


#faca uma pp que mostre o resultado da tabuada
# deve pedir o num pra faer a tabuada


# num = int(input("Introduz um numero: "))

# print (f"Tabuada do {num}:")

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
    
    
    
        
        
# while True:
#     print("Menu:")
#     print("1 - Olá Mundo")
#     print("2 - Bom Dia")
#     print("3 - Boa Noite")
#     print("0 - Sair")

#     opt = input("Escolha uma opção: ")

#     if opt == "0":
#         print("Adios")
#         break

#     match opt:
#         case "1":
#             print("Olá Mundo")
#         case "2":
#             print("Bom Dia")
#         case "3":
#             print("Boa Noite")
#         case _:
#             print("Opção inválida")


# nomes = []

# for i in range(1, 6):
#     nome = input(f"Introduza o {i}º nome: ")
#     nomes.append(nome)
    
# print("\nLista")
# for n in nomes:
#     print(n)
    
    
    # crie um programa que peça ao user nomes ate ser introduzido "0"
    # e mostre os nomes 1 por linha
    
nomes = []

while True:
    nome = input("Introduz um nome (0 para sair e listar os nomes): ")
    
    if nome == "0":
        break
    
    nomes.append(nome)
    
print("\nNomes: ")
for n in nomes:
    print(n)