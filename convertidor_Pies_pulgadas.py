print ("CONVERTIDOR DE PIES Y PULGADAS A CENTIMETROS")

_pie = int(input("Ingrese la cantidad de pies: "))
resul_pie = _pie * 12
pie_cm = resul_pie * 2.54

_pulgadas = int(input("Ingrese la cantidad de pulgadas: "))
resul_pulgada = _pulgadas *2.54

_total = pie_cm + resul_pulgada

print(f"{_pie} pies y {_pulgadas} pulgadas son: {_total} ")




