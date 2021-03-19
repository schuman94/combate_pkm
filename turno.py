from pokemon import Pokemon
from movimientos import Movimiento
import random

class Turno:
    __contador = 0

    def __init__(self, pokemon_jugador: Pokemon, pokemon_rival: Pokemon, accion_jugador, accion_rival):
        self.__numero = Turno.__contador
        Turno.__contador += 1
        self.__pokemon_jugador = pokemon_jugador
        self.__pokemon_rival = pokemon_rival
        self.__accion_jugador = accion_jugador
        self.__accion_rival = accion_rival
        self.__set_diccionario_ataques(self.__pokemon_jugador, self.__pokemon_rival, self.__accion_jugador, self.__accion_rival)

    def __set_diccionario_ataques(self, pokemon_jugador, pokemon_rival, accion_jugador, accion_rival):
        """Crea un diccionario con claves (pokemon) y valores (movimientos)"""
        self.__diccionario_ataques = {}
        self.__diccionario_ataques[pokemon_jugador] = accion_jugador
        self.__diccionario_ataques[pokemon_rival] = accion_rival

    def __get_diccionario_ataques(self):
        """Devuelve el diccionario de ataques"""
        return self.__diccionario_ataques

    def get_numero(self):
        return self.__numero

    def prioridad(self):
        """Comprueba si hay un cambio de pokemon, si no, devuelve el pokemon mas rapido"""
        #if type(self.__accion_jugador) == Movimiento:
        return self.pokemon_mas_rapido()
        #Pendiente implementar el cambio de pokemon


    def pokemon_mas_rapido(self):
        """Devuelve el pokemon más rapido"""
        if self.__pokemon_jugador.get_velocidad() > self.__pokemon_rival.get_velocidad():
            return self.__pokemon_jugador
        elif self.__pokemon_jugador.get_velocidad() == self.__pokemon_rival.get_velocidad():
            return random.choice([self.__pokemon_jugador, self.__pokemon_rival])
        else:
            return self.__pokemon_rival


    def ejecutar(self):
        """Ejecuta el turno"""
        #pedirle al turno ordenar los pokemon por velocidad
        primero = self.prioridad()
        segundo = self.__pokemon_jugador if (primero == self.__pokemon_rival) else self.__pokemon_rival
        #ejecutar el primer movimiento
        primero.atacar(self.__get_diccionario_ataques()[primero])


        #comprobaciones
        #ejecutar el otro movimiento
        #comprobaciones
