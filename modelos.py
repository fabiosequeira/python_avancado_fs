# marca
# Modelo
# ano
# num_km

class Carro:
    
    def __init__(self, marca: str, modelo: str, ano: int, num_km: float, tanque_litros: float):   #self --> (this)
        self.marca = marca.capitalize()
        self.modelo = modelo.capitalize()
        self.ano = ano
        self.num_km = num_km
        self.tanque_litros = tanque_litros
        self.combustivel_atual = tanque_litros  # começa cheio
        self.km_inicial = num_km
        self.combustivel_usado = 0  
        
    def mudar_cor(self, cor: str):
        self.cor = cor.capitalize()
        
    def andar(self, velocidade: int, tempo: int, combustivel_atual: float):
        distancia = velocidade * (tempo / 60)  # passar os minutos pra horas
        self.num_km += distancia

        # Atualiza o combustível usado no objeto
        self.combustivel_usado = self.tanque_litros - combustivel_atual

        return distancia, combustivel_atual
    
    def calcular_consumo(self):
        km_percorridos = self.num_km - self.km_inicial
        
        return (self.combustivel_usado / km_percorridos) * 100 # consumo aos 100
        
        
class Livro:
    
    def __init__(self, titulo: str, autor: str, ano: int, editora: str, 
                  num_paginas: int, genero: str, classificacao_etaria: int, rating: float):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano = ano
        self.editora = editora.title()
        self.num_paginas = num_paginas
        self.genero = genero.capitalize()
        self.classificacao_etaria = classificacao_etaria
        self.rating = rating
        
        
        
        
class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, peso: float, energia: int):
        self.nome = nome.title()
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.energia = 100  
        self.a_dormir = False
        
    def comer(self, alimento: list[str]):
        for item in alimento:
            self.peso += 100
    
    def falar(self):
        print("Olá, meu nome é " + self.nome)
    
    def andar(self):
        return "A pessoa está a andar"
    def envelhecer(self):
        self.idade += 1

        if self.idade <= 21:
            self.altura += 0.025
    def crescer(self):
        pass
    
    def dormir(self):
        self.energia = 100
        if not self.a_dormir:
            self.a_dormir = True
            print(f"{self.nome} foi dormir.")
        else:
            print(f"{self.nome} já está a dormir.")
    
    def acordar(self):
        if self.a_dormir:
            self.a_dormir = False
            self.energia = 100
            print(f"{self.nome} acordou cheio de energia!")
        else:
            print(f"{self.nome} já está acordado.")