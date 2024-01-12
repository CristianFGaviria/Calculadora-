import sys

print("CONVERTIDOR DE TIEMPO")
def salir ():
    print("Hasta la proxima!!! ")
    sys.exit()


while True:
    menu = """
    Cual de las siguientes opciones desea ejecutar
    [1] CONVERTIDOR DE SEGUNDOS A MINUTOS
    [2] CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS
    [3] SALIR

    """
    print(menu)

    opcion = int(input("Digite La opcion deseada: "))


    if opcion == 1:
        _segundos = int(input("Escriba la cantidad de segundos: "))
        _minuto = round(_segundos / 60)
        _segundero = _segundos % 60
        print (f"{_segundos} segundos son {_minuto} minutos y {_segundero} segundos ")
    elif opcion ==2:
        _seg = int(input("Escriba la cantidad de segundos: "))
        seg_conv = round(_seg / 3600) ## aqui estan las horas
        resto_seg = round(_seg % 3600) ## aqui se obtiene los segundos

        minutos = round(resto_seg / 60) ## Los minuntos de los segundos
        segundos = round(resto_seg % 60) ## Segundos de los minutos
        print(f"{_seg} segundos son {seg_conv} horas con {minutos} minutos y {segundos} segundos")


    elif opcion == 3:
        salir()
    else:
        print("Usted selecciono una opcion no valida. Intente nuevamente")