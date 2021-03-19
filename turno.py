class Turno:
    __contador = 0

    def __init__(self, accion_jugador, accion_rival):
        self.__numero = Turno.__contador
        Turno.__contador += 1
        self.__accion_jugador = accion_jugador
        self.__accion_rival = accion_rival


    def get_numero(self):
        return self.__numero
