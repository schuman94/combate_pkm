from abc import ABC, abstractmethod

class Pokemon:
    def __init__(self, tipo, vida, ataque, defensa, velocidad, estado=None):
        self.__tipo = tipo
        self.set_vida(vida)
        self.set_ataque(ataque)
        self.set_defensa(defensa)
        self.set_velocidad(velocidad)
        self.set_estado(estado)
        self.__movimientos = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_tipo(self):
        return self.__tipo

    def get_vida(self):
        return self.__vida

    def set_vida(self, vida):
        self.__vida = vida

    def get_ataque(self):
        return self.__ataque

    def set_ataque(self, ataque):
        self.__ataque = ataque

    def get_defensa(self):
        return self.__defensa

    def set_defensa(self, defensa):
        self.__defensa = defensa

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_movimientos(self):
        """Devuelve una lista que contiene los 4 movimientos del pokemon"""
        return self.__movimientos

    def __str__(self):
        return self.get_nombre()

    def __repr__(self):
        return self.get_nombre()[0].upper() + self.get_nombre()[1:] + '(' \
               + self.get_tipo() + ', ' + str(self.get_vida()) + ', ' + str(self.get_ataque()) \
               + ', ' + str(self.get_defensa()) + ', ' + str(self.get_velocidad()) + ', ' + 'estado=' + str(self.get_estado()) + ')'


    def set_movimientos(self, mov1, mov2, mov3, mov4):
        """Añade los 4 movimientos correspondientes al pokemon"""
        self.__movimientos.append(mov1)
        self.__movimientos.append(mov2)
        self.__movimientos.append(mov3)
        self.__movimientos.append(mov4)

    def mostrar_movimientos(self):
        """Imprime en la salida los 4 movimientos disponibles"""
        contador = 1
        for i in self.get_movimientos():
            print(str(contador) + ': ' + str(i))
            contador += 1

    def atacar(self, mov):
        """El pokemon usa el ataque indicado y lo imprime en la salida"""
        print(self.get_nombre() + ' usa ' + self.get_movimientos()[mov].usar())
