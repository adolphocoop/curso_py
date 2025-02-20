#La clase se puede llamar como sea
class Vehiculos():

    #Creamos el constructor
    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    #Definir comportamientos o funcionalidades

    def arrancar(self):

        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frena(self):
        self.frena=True
    #\n sirve para dar saltos de linea
    def estado(self):
        print ("Marca;", self.marca, "\nModelo:", self.modelo, "\En Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena )


#La clase moto debe herar las propiedades y metodos


class Moto(Vehiculos):
    pass  

        