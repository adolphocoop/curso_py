print("Hola bienvenido, ingresa dos numeros por favor:  ")

num1=int(input("introduce el primer numero:  "))
num2=int(input("introduce el segundo numero:  "))

def DevuelveMax(num1, num2):
    if num1<num2:
        print(num2)
    elif num2<num1:
        print(num1)
    else:
        print("Los numeros son iguales")
    
print("El numero mas alto es:  ")

DevuelveMax(num1, num2 )

