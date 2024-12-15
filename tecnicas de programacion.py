"tecnica de programacion"

class animal:
    def __init__(self, nombre):
        self.nombre = nombre
        def dialogar(self):
            pass
# implementaremos en la subclase del metodo abstracto
class perro(animal):
    def dialogar(self):
        print("Guau Guau!")
class Gato(animal):
    def dialogar(self):
        print("Miauu Miauu!")
class cerdo(animal):
    def dialogar(self):
        print("Oing Oing!")
# creacion de nombres
Perro=perro("Max")
Gato=Gato("Zeus")
Cerdo=cerdo("Baby")

# metodo dialogar () para cada nombre
perro.dialogar("Guau Guau")

cerdo.dialogar("Oing Oing")