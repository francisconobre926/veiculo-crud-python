class Carro:
    
    def __init__(self, anoDeFabrico, modelo,marca, cor, motorista):
        self.id=+1  # Simplesmente incrementa o ID para cada novo carro
        self.anoDeFabrico=anoDeFabrico
        self.modelo=modelo
        self.marca=marca
        self.cor=cor
        self.motorista=motorista
 
    def mostrarDetalhes(self):
        return (f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.anoDeFabrico}, Cor: {self.cor}, Motorista responsavel:{self.motorista}")

    