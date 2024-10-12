#ENTRADA
lado = int(input("Ingrese el lado del hexágono: "))

#PROCESO
area = lado**2 * (3 * 3**0.5) / 2
area_aprox = round(area, 3)

#SALIDA
print("El área es", str(area_aprox))
