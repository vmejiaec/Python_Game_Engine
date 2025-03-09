from game_engine import Game_Engine
from personajes import Personaje

class Main:
    def __init__(self):
        self.engine = Game_Engine(fps=5)
        self.ciclos =0 
        self.ciclos_max = 15

        self.player = Personaje(nombre="Qio")

    def init(self):
        print("init")

    def update(self, delta_time):
        #Condición de parada por número de ciclos
        self.ciclos += 1
        if self.ciclos >= self.ciclos_max:
            self.engine.stop()
        print("Ciclo No: ", self.ciclos, "--------------------------")

        

        print("update", delta_time)

    def render(self):
        print("render")

    def run(self):
        print("run")
        self.engine.init= self.init
        self.engine.update=self.update
        self.engine.render= self.render

        self.engine.run()

if __name__ == "__main__":
    main = Main()
    main.run()
