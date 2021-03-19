class Turno:
    __contador = 0

    def __init__(self):
        self.__numero = Turno.__contador
        Turno.__contador += 1


    def get_numero(self):
        return self.__numero
