# Escribir un programa que pida al usuario un número entero positivo
# mayor que 2 y muestre por pantalla si es un número primo o no.

num = int(input("Introduce un número entero positivo mayor que 2: "))
es_primo = True
if num < 2:
    es_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")