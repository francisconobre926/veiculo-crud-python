class Carro:
    id=0
    def __init__(self, anoDeFabrico, modelo,marca, cor, motorista):
        Carro.id += 1
        self.id =Carro.id 
        self.anoDeFabrico=anoDeFabrico
        self.modelo=modelo
        self.marca=marca
        self.cor=cor
        self.motorista=motorista
 
    def mostrarDetalhes(self):
        return (f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.anoDeFabrico}, Cor: {self.cor}, Motorista responsavel:{self.motorista}")

    