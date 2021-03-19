from entrenador import Entrenador
from pokemon import Pokemon
from pokedex import *
from movimientos import *
import random
from combate import Combate

disponibles = ['vaporeon', 'flareon', 'jolteon', 'eevee']
disponibles_jugador = disponibles[::]
disponibles_rival = disponibles[::]

def mostrar_disponibles(lista):
    for i in lista:
        print(i)

def quitar_disponible(nombre, lista):
    lista.remove(nombre)

def despachar_pokemon(pk, lista):
    """Devuelve el pokemon seleccionado"""
    if pk not in lista:
        raise ValueError('El pokemon elegido no se encuentra disponible')
    elif pk == 'vaporeon':
        quitar_disponible('vaporeon', lista)
        return Vaporeon()
    elif pk == 'flareon':
        quitar_disponible('flareon', lista)
        return Flareon()
    elif pk == 'jolteon':
        quitar_disponible('jolteon', lista)
        return Jolteon()
    elif pk == 'eevee':
        quitar_disponible('eevee', lista)
        return Eevee()


def seleccionar_pokemon(lista):
    """Devuelve una lista con 3 instancias de la clase Pokemon"""
    pk1 = None
    pk2 = None
    pk3 = None

    seleccion = [pk1, pk2, pk3]
    contador = 0

    while contador < 3:
        try:
            seleccion[contador] = despachar_pokemon(input('Elige un pokemon: '), lista)
        except ValueError:
            print('\nEl pokemon elegido no se encuentra disponible. Elige uno de los siguientes:')
            mostrar_disponibles(lista)
        else:
            contador += 1
        finally:
            print()
            continue
    return seleccion

def seleccionar_pokemon_rival(lista):
    seleccion = []
    for i in range(0, 3):
        aleatorio = random.choice(lista)
        poke = despachar_pokemon(aleatorio, lista)
        seleccion.append(poke)
    return seleccion


print('Hola entrenador, preparate para combatir!\n')
print('Pokemon disponibles:')
mostrar_disponibles(disponibles_jugador)
print()

equipo = seleccionar_pokemon(disponibles_jugador)
equipo_rival = seleccionar_pokemon_rival(disponibles_rival)

jugador = Entrenador(equipo[0], equipo[1], equipo[2])
rival = Entrenador(equipo_rival[0], equipo_rival[1], equipo_rival[2])

combate = Combate(jugador, rival)

while not combate.get_terminado():
    combate.siguiente_turno()
