class Motorista:

    def  __init__(self, nome, idade):
        self.motorista_id = +1
        self.nome=nome
        self.idade=idade
       

    def __str__(self):
        return f"nome: {self.nome} ({self.idade} anos de idade)"    
