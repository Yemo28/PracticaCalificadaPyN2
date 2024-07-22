# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital
# obtenido en la inversión cada año que dura la inversión.

cantidad = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual: "))
años = int(input("Introduce el número de años: "))

for año in range(1, años + 1):
    cantidad+=cantidad*interes_anual
    print("El año: ", año, "la cantidad fue: ", cantidad)