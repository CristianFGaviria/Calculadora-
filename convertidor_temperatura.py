import sys


print("CONVERTIDOR DE TEMPERATURAS ")

def salir ():
    print("Hasta la proxima!!! ")
    sys.exit()

while True:
    menu = """
    Cual de las siguientes opciones desea ejecutar
    [1] CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT
    [2] CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS
    [3] SALIR
    
    """
    print(menu)

    opcion = int(input("Digite La opcion deseada: "))
    if opcion == 1:
        _grados_cel = float(input("Ingrese los grados CELSIUS: "))
        _fahrenheit = 1.8 * _grados_cel + 32
        print(f"de {_grados_cel}ºC son {_fahrenheit}ºF ")

    elif opcion ==2:
        _grados_fah = float(input("Ingrese los grados FAHRENHEIT: "))
        _celcius = round((_grados_fah - 32)/1.8,1)
        print(f"de {_grados_fah}ºF son {_celcius}ºC ")
    elif opcion == 3:
        salir()
    else:
        print("Usted selecciono una opcion no valida. Intente nuevamente")

