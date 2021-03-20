from abc import ABC, abstractmethod
import random

class Pokemon:
    def __init__(self, tipo, vida, ataque, defensa, velocidad, estado=None, owner=None):
        self.__tipo = tipo
        self.set_vida(vida)
        self.set_ataque(ataque)
        self.set_defensa(defensa)
        self.set_velocidad(velocidad)
        self.set_estado(estado)
        self.set_owner(owner)
        self.__movimientos = []

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    def get_nombre(self):
        return self.__nombre

    def get_nombre_completo(self):
        if self.get_owner() == 'rival':
            return self.get_nombre() + ' enemigo'
        return self.get_nombre()

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
        if self.get_owner() == 'rival':
            return self.get_nombre() + ' enemigo'
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
        """
        Devuelve un diccionario que contiene la potencia y el efecto del ataque.
        Si falla devuelve None.
        """
        indice = self.get_movimientos().index(mov)
        ataque = self.get_movimientos()[indice]
        potencia = ataque.get_potencia()
        precision = ataque.get_precision()
        efecto = ataque.get_efecto()
        print(self.get_nombre_completo() + ' usa ' + ataque.get_nombre(), end=' -> ')
        ataque.usar()
        if random.randint(1, 100) > precision:
            print('Pero falló', end=' -> ')
            return None
        else:
            return {'potencia': potencia, 'efecto': efecto}
