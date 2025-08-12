from factory import carroFactory

class CarroService:

    def __init__(self):
        self.carros = []


    def adicionarCarro(self):
        carro = carroFactory()
        self.carros.append(carro)

    def listarCarros(self):
        for carro in self.carros:
            print(carro.mostrarDetalhes())
            print("-" * 90)

        else:
            print("Nenhum carro cadastrado.")

    def removerCarro(self,id):
        for carro in self.carros:
            if carro.id==id:
                self.carros.remove(carro)
                return carro
        else:
            print("o carro pretendido nao existe")    
    
