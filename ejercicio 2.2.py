#ENTRADA
q1 = float(input("Ingrese valor de la primera carga: "))
q2 = float(input("Ingrese valor de la segunda carga: "))
r = float(input("Ingrese la distancia entre las cargas: "))

#PROCESO
fuerza = (q1 * q2) / (r ** 2)
fuerza_final = round(fuerza, 10)

#SALIDA
print("La fuerza es:", str(fuerza_final))
