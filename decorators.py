def atencion (f):
    def wrapper(): #wrapper significa envoltorio. Pero podría ser cualquier nombre
        print("Comienza a correr la función..." )
        f()
        print("Terminó la función")
    return wrapper()

@atencion
def hello():
    print("Esta es la función envuelta")

hello()