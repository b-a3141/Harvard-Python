#creo la clase Point
class Point():
#defino cómo van a ser sus elementos
    def __init__(self, x, y):
        self.x = x
        self.y = y
#Creo un nuevo elemento de la clase
p = Point(-5, 12)



print(p.x , p.y)

#creo la clase Flyght
class Flyght():
    def __init__(self, capaciti):
        self.capaciti = capaciti
        self.passengers = []
#creo una función dentro de esta clase para ir asignando la lista de pasajeros
#además una función para controlar que no se supere la disponibilidad
    def add_passangers(self, name):
        if (self.capaciti - len(self.passengers)) >= 1: # es equivalente a open_seats == 0
            self.passengers.append(name)
            return True
        else:
            return False
        
#creo una función dentro de esta clase para chequear los asientos disponibles
    def open_seats(self):
        return (self.capaciti - len(self.passengers))
#Creo un nuevo elemento de la clase
flyght973 = Flyght(5)

#Invento una lista de interesados en volar
people = ["A", "B", "C", "D", "E", "F","G"]
#creo un loop para ir asignando los asientos
for interesado in people:
  
    if flyght973.add_passangers(interesado):
        print(f"El pasajero {interesado} ha sido asignado satisfactoriamente")
    else:
        print(f"No hay asientos disponibles para {interesado} ")
    print(f"Quedan {flyght973.open_seats()} asientos disponibles")
