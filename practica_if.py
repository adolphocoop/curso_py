#Creamos una funcion
#Operadores de comparacion < menor que, >mayor que
# Igual que ==, <= menor o igual, >=maypr igual que

print("Programa de evalucion de notas de alumnos")

nota_alumno=int(input("Introduce la nota:  "))

def evaluacion(nota):
    valoracion="aprobado"
    #condicional 
    if nota<5:
        valoracion="reprobado"
    return valoracion


print(evaluacion(nota_alumno))