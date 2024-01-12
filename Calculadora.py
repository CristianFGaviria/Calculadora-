import sys

def suma ():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resultado = numero1 + numero2
    print(f"El resultado de la operacion es = {resultado}")
def resta ():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resultado = numero1 - numero2
    print(f"El resultado de la operacion es = {resultado}")
def multiplica ():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resultado = numero1 * numero2
    print(f"El resultado de la operacion es = {resultado}")
def divide ():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resultado = numero1 / numero2
    print(f"El resultado de la operacion es = {resultado}")

def media_aritmetica ():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resultado = (numero1 + numero2)/2
    print(f"El resultado de la media aritmetica de los numeros {numero1} y {numero2} es = {resultado}")

def salir ():
    print("Hasta la proxima!!! ")
    sys.exit()

print("Bienvenido a la calculadora en Python")
while True:
    menu = """
    Cual de las siguientes opciones desea ejecutar
    [1] Sumar
    [2] Restar
    [3] Multiplicar
    [4] Dividir
    [5] Media Aritmetica
    [6] Salir
    """

    print(menu)

    opcion = int(input("Digite La opcion deseada: "))
    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplica()
    elif opcion == 4:
        divide ()
    elif opcion == 5:
        media_aritmetica()
    elif opcion == 6:
        salir()
    else:
        print("Usted selecciono una opcion no valida. Intente nuevamente")


