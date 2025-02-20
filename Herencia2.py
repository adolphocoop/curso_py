class Vehiculo():

    #Constructor

    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    #Comportamientos o funciones
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelerar=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print ("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena )
        
class Furgoneta(Vehiculo):
    #Metodo
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La Furgoneta esta cargada"
        else: 
            return "La furgoneta no esta cargada"


class Moto(Vehiculo):
    #Propiedad
    hcaballito=""

    #Creamos un metodo
    def caballito(self):
        self.hcaballito="Voy haciendo caballito"
    
    def estado(self):
        print ("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena )

class VElectrico():
    #Constructor
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        
        self.cargando=True






#Creamos un ejemplo o instancia
#Esta instancia hereda de la case vehiculo
miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

#Creamos una instancia 
miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectrico, Vehiculo):
    pass

miBici=BicicletaElectrica()