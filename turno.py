from pokemon import Pokemon
from movimientos import Movimiento
from tipos import *
import random

class Turno:
    __contador = 0

    def __init__(self, pokemon_jugador: Pokemon, pokemon_rival: Pokemon, accion_jugador, accion_rival):
        Turno.__contador += 1
        self.__numero = Turno.__contador
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
        """Devuelve el pokemon mas rapido o el unico atacante"""
        if self.__get_diccionario_ataques()[self.__pokemon_jugador] == 'cambio':
            return self.__pokemon_rival
        else:
            return self.pokemon_mas_rapido()


    def pokemon_mas_rapido(self):
        """Devuelve el pokemon más rapido"""
        if self.__pokemon_jugador.get_velocidad() > self.__pokemon_rival.get_velocidad():
            return self.__pokemon_jugador
        elif self.__pokemon_jugador.get_velocidad() == self.__pokemon_rival.get_velocidad():
            return random.choice([self.__pokemon_jugador, self.__pokemon_rival])
        else:
            return self.__pokemon_rival

    def calculo_damage(self, atacante: Pokemon, receptor: Pokemon, datos_ataque):
        """
        Devuelve una lista que contiene:
        0 -> un entero con la cantidad de daño que ocasiona el ataque.
        1 -> 'Es muy eficaz' , 'Es poco eficaz', ''
        """
        ####################ALGORITMO DAÑO######################
        elemento_ataque = datos_ataque['tipo']
        elemento_atacante = atacante.get_tipo()
        elemento_receptor = receptor.get_tipo()

        B = 1.5 if elemento_atacante.get_elemento() == elemento_ataque.get_elemento() else 1

        if elemento_receptor.get_elemento() in elemento_ataque.get_eficaz():
            E = 2
            eficacia = ' ->  Es muy eficaz'
        elif elemento_receptor.get_elemento() in elemento_ataque.get_no_eficaz():
            E = 0.5
            eficacia = ' ->  Es poco eficaz'
        else:
            E = 1
            eficacia = ''

        V = random.randint(85, 100)
        N = 100 #Nivel del pokemon
        A = atacante.get_ataque()
        P = datos_ataque['potencia']
        D = receptor.get_defensa()

        damage = [int(0.01 * B * E * V * (((0.2 * N + 1) * A * P) / (25 * D) + 2)), eficacia]
        return damage

    def ejecutar(self):
        """
        Ejecuta el turno.
        Devuelve None si no hay pokemon eliminado.
        Devuelve un pokemon si ha sido eliminado.
        """
        eliminado = None
        #pedirle al turno ordenar los pokemon por velocidad
        primero = self.prioridad()
        segundo = self.__pokemon_jugador if (primero == self.__pokemon_rival) else self.__pokemon_rival
        #ejecutar el primer movimiento
        datos_ataque = primero.atacar(self.__get_diccionario_ataques()[primero])
        if datos_ataque != None:
            damage = self.calculo_damage(primero, segundo, datos_ataque)
            segundo.set_vida(segundo.get_vida() - damage[0])
            print(damage[1], end='  ->  ') #Esto es la cadena que indica si es eficaz
        #comprobaciones
        if segundo.get_vida() < 0:
            segundo.set_vida(0)
        print(f'{segundo.get_nombre_completo()} | PS:{segundo.get_vida()}\n')
        if segundo.get_vida() == 0:
            eliminado = segundo
            print(segundo.get_nombre_completo() + ' se ha debilitado')
            print()
            return eliminado
        if self.__get_diccionario_ataques()[self.__pokemon_jugador] != 'cambio':
            #ejecutar el otro movimiento
            datos_ataque = segundo.atacar(self.__get_diccionario_ataques()[segundo])
            if datos_ataque != None:
                damage = self.calculo_damage(segundo, primero, datos_ataque)
                primero.set_vida(primero.get_vida() - damage[0])
                print(damage[1], end='  ->  ') #Esto es la cadena que indica si es eficaz
            #comprobaciones
            if primero.get_vida() < 0:
                primero.set_vida(0)
            print(f'{primero.get_nombre_completo()} | PS:{primero.get_vida()}\n')
            if primero.get_vida() == 0:
                eliminado = primero
                print(primero.get_nombre_completo() + ' se ha debilitado')
                print('_________________________________________________________________________ \n')
                print()
                return eliminado
        print('_________________________________________________________________________ \n')
        return eliminado

#SERGIO CHULIAN MANTEL
