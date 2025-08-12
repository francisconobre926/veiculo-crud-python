import os
from carroService import CarroService
from Motorista import Motorista
from Carro import Carro
from motoristaService import MotoristaService
from motoristaService import MotoristaService
from factory import carroFactory, motoristaFactory

servico = CarroService()


def limpar_tela():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')

def camposParaActualizarMotorista():
   pass
    

def processarEscolha(escolha):
        match escolha:
            case "1":
                carro = carroFactory()
                servico.adicionarCarro(carro)    
            case "2":
                servico.listarCarros()
            case "3":
                id=int(input("digite o id do carro a remover"))
                servico.removerCarro(id)  
            case "4":
                id=int(input("Digite o ID do carro a actulizar: "))
                campos=camposParaActualizarMotorista()
                servico.actualizarMotorista(id,campos)
                
            case "5":
                print("Saindo do sistema...!")
                exit()     
            case _:
                print("Opção inválida. Tente novamente.")

def telaInicial():
    print("Bem-vindo ao Sistema de Gerenciamento!")
    print("1. Adicionar Carro")
    print("2. Listar Carros")
    print("3. Remover Carro")
    print("4. actualizar Motorista")
    print("5. Sair")
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

   

    
                            
                             