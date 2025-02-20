#Sintaxis para crear una clase, ejemplo clase para construir coches
class Coche():
    
    #Los objetos tienen estado, propiedades y comportamiento
    #Constructor de clase, dara el estado inicial
   def __init__(self):
    #1 Propiedades
     self.__largoChasis=250
     self.__anchoChasis=120
     self.__ruedas=4
     self.__enmarcha=False

    #Metodos

    # Self hace referencia al propio objeto, pass: 
    #Dependiendo de lo que se le pasa a la variable arrancamos
   def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        #Realizar el chequeo
        if(self.__enmarcha):
           chequeo=self.__chequeo_interno()
        #Agregamos la variable chequeo para ver si el coche ha arrancado.
        
        
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enmarcha and chequeo==False):
           return "Algo ha ido mal en el chequeo. no podemos arrancar"

        else: 
            return "El coche esta apagado"

    #Segundo metodo que solo imprime el estado del coche
   def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo ", self.__largoChasis)


   #Metodo para verificar niveles: Aceite, gasolina, agua
   
   #El metodo esta encapsulado
   def __chequeo_interno(self):
    print ("Realizando chequeo interno")

    self.gasolina="Ok"
    self.aceite="Ok"
    self.puertas="Cerradas"
    
    if(self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
       return True
    
    else:
       return False



#Crear los objetos
#instanciar una clase, ejemplarizar la clase o crear un ejemplar



miCoche=Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("-----------A continuacion creamos el segundo objeto-------- ")

miCoche2=Coche()
print(miCoche2.arrancar(False))
#Cambiamos el valor de la propiedad para ver que desde fuera se pueden modificar las propiedades
#miCoche2.ruedas=2
miCoche2.estado()