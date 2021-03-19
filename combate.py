from turno import Turno
from entrenador import Entrenador
import random

class Combate:
    def __init__(self, jugador: Entrenador, rival: Entrenador):
        self.__jugador = jugador
        self.__rival = rival
        self.__turno = None
        self.__terminado = False

    def get_jugador(self):
        """Devuelve al jugador"""
        return self.__jugador

    def get_rival(self):
        """Devuelve al rival"""
        return self.__rival

    def get_turno(self):
        """Devuelve el turno actual"""
        return self.__turno

    def get_terminado(self):
        """Devuelve False si el combate no ha terminado"""
        return self.__terminado

    def set_terminado(self):
        """Marcar como terminado el combate"""
        self.__terminado = True

    def pedir_accion(self):
        """Devuelve un movimiento (class Movimiento) o un cambio de pokemon"""
        opcion = 'atras'
        while opcion == 'atras':
            peticion = input(f'atacar o cambiar: ')
            print()
            if peticion == 'atacar':
                opcion = self.pedir_ataque()
            if peticion == 'cambiar':
                opcion = self.cambiar_pokemon()
        return opcion

    def pedir_ataque(self):
        """Devuelve un movimiento (class Movimiento) a partir de la lista de movimientos del pokemon"""
        self.get_jugador().pokemon_actual().mostrar_movimientos()
        print()
        ataque = input('Elige el movimiento (1, 2, 3, 4 o atras): ')
        print()
        if ataque == 'atras':
            mov = 'atras'
        elif ataque in '1234':
            mov = self.get_jugador().pokemon_actual().get_movimientos()[int(ataque) - 1]
        else:
            raise ValueError('Opcion no valida')
        return mov

    def seleccionar_ataque_rival(self):
        """Devuelve aleatoriamente un movimiento (class Movimiento) a partir de la lista de movimientos del pokemon del rival"""
        return random.choice(self.get_rival().pokemon_actual().get_movimientos())

    def __iniciar_turno(self):
        self.get_turno().ejecutar()


    def siguiente_turno(self):
        """
        Construye el siguiente turno a partir de:
        pokemon del jugador y rival
        accion del jugador y rival
        Luego inicia el turno
        """
        accion_jugador = self.pedir_accion()
        accion_rival = self.seleccionar_ataque_rival()
        self.__turno = Turno(self.get_jugador().pokemon_actual(), self.get_rival().pokemon_actual(), \
                             accion_jugador, accion_rival)
        self.__iniciar_turno()
