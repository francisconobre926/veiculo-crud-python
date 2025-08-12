import os
from carroService import CarroService
from Motorista import Motorista
from Carro import Carro
from motoristaService import MotoristaService
from motoristaService import MotoristaService

servico = CarroService()


def limpar_tela():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')


def processarEscolha(escolha):
        match escolha:
            case "1":
                servico.adicionarCarro()    
            case "2":
                servico.listarCarros()
            case "3":
                id=int(input("Digite o ID do carro a remover: "))
                servico.removerCarro(id)  
            case "4":
                print("Saindo do sistema...!")
                exit() 
            case _:
                print("Opção inválida. Tente novamente.")

def telaInicial():
    print("Bem-vindo ao Sistema de Gerenciamento!")
    print("1. Adicionar Carro")
    print("2. Listar Carros")
    print("3. Remover Carro")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    processarEscolha(escolha)


              

def menu():
    while True:
        telaInicial()
        continuar = input("Deseja continuar? (1.sim/2.nao): ")
        limpar_tela()
        if continuar.lower() != '1':
            print("Saindo do sistema. Até logo!")
            break

   

    
                            
                             