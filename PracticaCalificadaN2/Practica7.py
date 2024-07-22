# Escribir un programa que muestre por pantalla la tabla de multiplicar
# del 1 al 10.

num = int(input("Introduce un número: "))
multi = 0
i = 1
while i <= 10:
    multi = num * i
    print(f"{num} x {i} = {multi}")
    i += 1