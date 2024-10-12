#ENTRADA
lado_hexagono = float(input("Ingrese el lado del hexágono: ")) 

#PROCESO
area_hexagono = (lado_hexagono**2) * ((3 * (3**1 / 2)) / 2) 
area_hexagono_redondeada = round(area_hexagono, 3) 

#SALIDA
print("El área es ", area_hexagono_redondeada) 
