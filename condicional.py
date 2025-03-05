salario_presidente=int(input("Introduce salario presidente"))
#Para concatenar un string con un entero se usa STR antes de la variable a convertir
print("Salario presidente: " +str(salario_presidente))

salario_director=int(input("Introduce salario del director"))
#Para concatenar un string con un entero se usa STR antes de la variable a convertir
print("Salario Director: " +str(salario_director))

salario_jefe_area=int(input("Introduce salario del jefe de area"))
#Para concatenar un string con un entero se usa STR antes de la variable a convertir
print("Salario de Jefe de Area: " +str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario Administrativo"))
#Para concatenar un string con un entero se usa STR antes de la variable a convertir
print("Salario Administrativo: " +str(salario_administrativo))

#El siguiente if contiene una concatenacion de operadores de comparacion 

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo resulto mal")
