import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Solo se aceptan valores numéricos")
    sys.exit(1)

try:
    cociente = x/y
except ZeroDivisionError:
    print("No es posible dividir por cero")
    sys.exit(1)

print (f"El cociente entre {x} e {y} es {cociente} ")
