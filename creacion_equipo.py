from entrenador import Entrenador
from pokemon import Pokemon
from pokedex import *
from movimientos import *
import random
from combate import Combate

#Esto se tiene que convertir en una lista automatica
disponibles = ['vaporeon', 'flareon', 'jolteon', 'eevee', 'muk', 'snorlax', 'rattata', 'tangela']
disponibles_jugador = disponibles[::]
disponibles_rival = disponibles[::]

def mostrar_disponibles():
    """Imprime en la salida la lista de pokemon disponibles"""
    for i in disponibles_jugador:
        print(i)

def quitar_disponible(nombre, lista):
    """Quita de la lista de disponibles el pokemon seleccionado"""
    lista.remove(nombre)

def despachar_pokemon(pk, lista, owner):
    """Devuelve el pokemon seleccionado"""
    #Esto se tiene que convertir en un bucle for que recorra una lista de pokemon
    if pk not in lista:
        raise ValueError('El pokemon elegido no se encuentra disponible')
    elif pk == 'vaporeon':
        quitar_disponible('vaporeon', lista)
        return Vaporeon(owner)
    elif pk == 'flareon':
        quitar_disponible('flareon', lista)
        return Flareon(owner)
    elif pk == 'jolteon':
        quitar_disponible('jolteon', lista)
        return Jolteon(owner)
    elif pk == 'eevee':
        quitar_disponible('eevee', lista)
        return Eevee(owner)
    elif pk == 'muk':
        quitar_disponible('muk', lista)
        return Muk(owner)
    elif pk == 'snorlax':
        quitar_disponible('snorlax', lista)
        return Snorlax(owner)
    elif pk == 'rattata':
        quitar_disponible('rattata', lista)
        return Rattata(owner)
    elif pk == 'tangela':
        quitar_disponible('tangela', lista)
        return Tangela(owner)

def seleccionar_pokemon_jugador():
    """Devuelve una lista con 3 instancias de la clase Pokemon que será el equipo del jugador"""
    pk1 = None
    pk2 = None
    pk3 = None

    seleccion = [pk1, pk2, pk3]
    contador = 0

    while contador < 3:
        try:
            seleccion[contador] = despachar_pokemon(input('Elige un pokemon: '), disponibles_jugador, 'jugador')
            print('funcionaaa por ahoraaaaaaaaaaaaa')
        except ValueError:
            print('\nEl pokemon elegido no se encuentra disponible. Elige uno de los siguientes:')
            mostrar_disponibles()
        else:
            contador += 1
        finally:
            print()
            continue
    return seleccion

def seleccionar_pokemon_rival():
    """Devuelve una lista con 3 instancias de la clase pokemon que será el equipo del rival"""
    seleccion = []
    for i in range(0, 3):
        aleatorio = random.choice(disponibles_rival)
        poke = despachar_pokemon(aleatorio, disponibles_rival, 'rival')
        seleccion.append(poke)
    return seleccion
