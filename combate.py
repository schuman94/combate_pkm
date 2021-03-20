from turno import Turno
from entrenador import Entrenador
import random

class Combate:
    def __init__(self, jugador: Entrenador, rival: Entrenador):
        self.__jugador = jugador
        self.__rival = rival
        self.__turno = None
        self.__terminado = False
        self.__ganador = None

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

    def set_ganador(self, entrenador: Entrenador):
        """Confirma el ganador"""
        print('GANADOR: ' + entrenador.get_nombre().upper())

    def pedir_accion(self):
        """Devuelve un movimiento (class Movimiento) o un cambio de pokemon"""
        opcion = 'atras'
        while opcion == 'atras':
            peticion = input(f'atacar o cambiar: ')
            print()
            if peticion == 'atacar':
                opcion = self.pedir_ataque()
            if peticion == 'cambiar':
                print('Tu equipo:')
                self.get_jugador().equipo()
                pk = input('Selecciona el pokemon o vuelve atras: ')
                print()
                if pk == 'atras':
                    continue
                try:
                    self.get_jugador().cambiar(pk)
                    opcion = 'cambio'
                except ValueError:
                    print('No tienes ese pokemon o ya se encuentra en combate.\n')
                    continue
        return opcion

    def pedir_ataque(self):
        """Devuelve un movimiento (class Movimiento) a partir de la lista de movimientos del pokemon"""
        while True:
            self.get_jugador().pokemon_actual().mostrar_movimientos()
            print()
            ataque = input('Elige el movimiento (1, 2, 3, 4 o atras): ')
            print()
            if ataque == 'atras':
                mov = 'atras'
            elif ataque in '1234':
                mov = self.get_jugador().pokemon_actual().get_movimientos()[int(ataque) - 1]
                if mov.get_pp() < 1:
                    print('NO QUEDAN PP\'s\n')
                    continue
            else:
                print('Opción no valida.\n')
                continue
            return mov

    def seleccionar_ataque_rival(self):
        """Devuelve aleatoriamente un movimiento (class Movimiento) a partir de la lista de movimientos del pokemon del rival"""
        return random.choice(self.get_rival().pokemon_actual().get_movimientos())

    def __iniciar_turno(self):
        """
        Inicia el turno, lo ejecuta.
        Devuelve None si ambos pokemo siguen vivos.
        Devuelve un pokemon si ha sido eliminado.
        """
        return self.get_turno().ejecutar()

    def __finalizar_turno(self, eliminado):
        """
        Comprueba si a alguno de los entrenadores le quedan mas pokemon.
        Realiza el cambio o finaliza el combate.
        """
        if eliminado != None:
            #eliminar pokemonactual del entrenador y eliminarlo de su equipo
            entrenador_con_pokemon_eliminado = self.get_rival() if eliminado.get_owner() == 'rival' else self.get_jugador()
            entrenador_con_pokemon_eliminado.eliminar_pokemon_actual()
            entrenador_con_pokemon_eliminado.eliminar_pokemon(eliminado)
            #Si quedan pokemon en su equipo:
            if len(entrenador_con_pokemon_eliminado.get_equipo()) > 0:
                #Asignar un nuevo pokemonactual al entrenador de los que quedan en su equipo
                if entrenador_con_pokemon_eliminado.get_nombre() == 'rival':
                    nuevo_pokemon = random.choice(list(entrenador_con_pokemon_eliminado.get_equipo().values()))
                    entrenador_con_pokemon_eliminado.cambiar(nuevo_pokemon.get_nombre())
                elif entrenador_con_pokemon_eliminado.get_nombre() == 'jugador':
                    while True:
                        print('Equipo:')
                        entrenador_con_pokemon_eliminado.equipo()
                        pk = input('Selecciona el pokemon: ')
                        try:
                            entrenador_con_pokemon_eliminado.cambiar(pk)
                            break
                        except ValueError:
                            print('No tienes ese pokemon\n')
                            continue

            #Si no quedan pokemon en su equipo:
            if len(entrenador_con_pokemon_eliminado.get_equipo()) == 0:
                self.set_terminado()
                self.finalizar_combate(entrenador_con_pokemon_eliminado)


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
        print('TURNO ' + str(self.__turno.get_numero()) + '\n')
        eliminado = self.__iniciar_turno()
        self.__finalizar_turno(eliminado)

    def finalizar_combate(self, perdedor: Entrenador):
        """Recibe el entrenador perdedor y confirma el ganador"""
        if perdedor.get_nombre() == 'rival':
            self.set_ganador(self.get_jugador())
        elif perdedor.get_nombre() == 'jugador':
            self.set_ganador(self.get_rival())

#SERGIO CHULIAN MANTEL
