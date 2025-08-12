from Motorista import Motorista
from Carro import Carro


def carroFactory():
    anoDeFabrico = input("Digite o ano de fabrico do carro: ")
    modelo = input("Digite o modelo do carro: ")
    marca = input("Digite a marca do carro: ")
    cor = input("Digite a cor do carro: ")
    nome = input("Digite o nome do motorista: ")
    idade = input("Digite a idade do motorista: ")

    motorista = Motorista(nome, idade)
    carro = Carro(anoDeFabrico, modelo, marca, cor, motorista)

    return carro

def motoristaFactory():
    nome = input("Digite o nome do motorista: ")
    idade = input("Digite a idade do motorista: ")

    motorista = Motorista(nome, idade)

    return motorista