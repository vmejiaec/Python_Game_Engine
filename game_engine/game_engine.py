import time
from .ventana import Ventana

class Game_Engine:
    def __init__(self, fps = 15, ventana_ancho = 500, ventana_alto = 500, ventana_titulo = "Game Engine"):
        self.running = False
        #fps
        self.fps = fps
        self.delta_time = 0
        self.last_time = time.time()
        #ventana
        self.ventana = Ventana(ventana_titulo, ventana_ancho, ventana_alto)

    def run(self):
        self.running = True
        self.ventana.mostrar()
        self.init()
        while self.running:
            current_time = time.time()
            self.delta_time = current_time - self.last_time
            if (self.delta_time >= 1.0 / self.fps):
                self.update(self.delta_time)
                self.render()
                self.last_time = current_time
            else:
                time.sleep(max(0, 1.0 / self.fps - self.delta_time))

    def stop(self):
        self.running = False

    def init(self):
        pass

    def update(self, delta_time):
        pass

    def render(self):
        pass

    

    