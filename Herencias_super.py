class Persona():

    #Construir el metodo constructor
    #Les da un estado inicial  a los objectos tipo persona un nombre, edad y lugar de residencia
    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        #Imprime cuales son los valores de las siguientes propiedades
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        
#Vamos a decirle al constructor que va arecibir los siguientes datos
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario

        self.antiguedad=antiguedad 
    
    def descripcion(self):
        super().descripcion()

        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

#Construimos el objeto tipo persona, a la hora de llamar al constructor
#se le pasan los parametros

Manuel=Empleado(1600, 10, "Manuel", 55, "Colombia")
Manuel.descripcion()