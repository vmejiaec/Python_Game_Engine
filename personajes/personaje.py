
class Personaje:
    def __init__(self, nombre, vida=100, ataque=50):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        # Posición y tamaño
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10

    def __str__(self):
        print(f"Nombre: {self.nombre}")