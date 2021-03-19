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
        return self.__jugador

    def get_rival(self):
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
        peticion = input('Atacar o cambiar: ')
        if peticion == 'atacar':
            self.pedir_ataque()
        if peticion == 'cambiar':
            self.cambiar_pokemon()

    def pedir_ataque(self):
        """Devuelve un movimiento (class Movimiento) a partir de la lista de movimientos del pokemon"""
        ataque = input('Elige el movimiento: ')
        return self.get_jugador().pokemon_actual().get_movimientos()[int(ataque) - 1]

    def seleccionar_ataque_rival(self):
        """Devuelve aleatoriamente un movimiento (class Movimiento) a partir de la lista de movimientos del pokemon del rival"""
        return random.choice(self.get_rival().pokemon_actual().get_movimientos())

    def siguiente_turno(self):
        """Construye el siguiente turno a partir de la accion del jugador"""
        accion_jugador = self.pedir_accion()
        accion_rival = self.seleccionar_ataque_rival()
        self.__turno = Turno(accion_jugador, accion_rival)
        #pedir accion
        #elegir primer atacante
        #atacar
        #if vida de pokemon = 0, comprobar equipo: if equipo = 0, gameover, else: cambiar pokemon, else atacar
        #if vida de pokemon = 0, comprobar equipo: if equipo = 0, gameover, else: cambiar pokemon, else FIN


        if len(self.get_jugador().get_equipo()) == 0:
            pass
