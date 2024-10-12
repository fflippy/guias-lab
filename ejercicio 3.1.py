# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
#
# AUTOR
# NOMBRE:
# RUN:
# CARRERA:

#ENTRADA
caracter = input("Ingrese un cáracter: ")

#PROCESO y SALIDA
vocales = "aeiou"

if caracter in vocales:
    print("vocal")
elif caracter.isalpha() and caracter != vocales:
    print("consonante")
else:
    print("otro")
    
