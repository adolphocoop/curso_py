class Coche():
    #Para crear un contructor se utiliza __init__ que significa estado inicial
    def __init__(self):
    
        #Propiedades
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha= False
    
    #Creamos las funciones o metodos
    #El metodo arrancar recibirá dos parametros, depende de lo que le pasemos
    #Comportamientos
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            #Guardar en la variuable lo que devuelve la funcion chequeo
            chequeo=self.__chequeo_interno()


        #comprobar si ese coche tiene chequeo, se agrega la variable chequeo
        if(self.__enmarcha and chequeo):
            return "El cohce esta en marcha"
        #Comprobar si marcha es igual a True
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche esta parado"
    def estado(self):
        print("el coche tiene ", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de ", self.__largoChasis)


   #Crear metodo de chequeo 
   #Para encapsular un metodo se utiliza doble guion bajo para encapsular ese funsion
    def __chequeo_interno(self):
        print("Realizado chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"    
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
          return True

        else:
           return False


miCoche=Coche()
print(miCoche.arrancar(True)) # el metodo arrancar espera un parametro, de lo contario dara un error
miCoche.estado() 

print("--------A continuacion creamos el segundo objeto--------")
#Vamos a crear la segunda instancia

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

#Construrctor: Un metodo especial que le da estado inicial a un objeto.

#Encapsulamiento de metodos
#Poner dos guion bajo indica el encapsulamiento



