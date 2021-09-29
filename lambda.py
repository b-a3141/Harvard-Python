people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Hermione", "house": "Griffindor"},
    {"name": "Drake", "house":"Slythein"},
    {"name":"Cho", "house": "Ravenclaw"}
]

def prioridad(persona):
    return persona["house"]

people.sort(key=prioridad)

print(people)

people.sort(key=lambda sujeto: sujeto["name"] )
print(people)
