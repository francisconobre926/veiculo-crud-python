from Motorista import Motorista
class MotoristaService:
    def __init__(self):
        self.motoristas=[]

   

    def adicionarMotorista(self, nome, idade):
        motorista=Motorista(nome, idade)
        self.motoristas.append(motorista)
        return motorista
    
    def listarMotoristas(self):
        for motorista in self.motoristas:
            print(motorista)
            print("-" * 90)

    