class Teclado:
    def mover_player(self, key, player, paso):
        if key == "w":
            print("Arriba")
            player.y -= paso
        elif key == "s":
            print("Abajo")
            player.y += paso
        elif key == "a":
            print("Izquierda")
            player.x -= paso
        elif key == "d":
            print("Derecha")
            player.x += paso
    
    def controles(self, key):
        if key == 'q':
            return 'Salir'
        elif key == 'e':
            return 'Atacar'
        elif key == 'r':
            return 'Recargar'
        elif key == 'f':
            return 'Usar'
        elif key == 'g':
            return 'Coger'
        elif key == 't':
            return 'Tirar'
        elif key == 'i':
            return 'Inventario'
        elif key == 'c':
            return 'Cerrar'
        elif key == 'm':
            return 'Mapa'
        elif key == 'h':
            return 'Ayuda'
