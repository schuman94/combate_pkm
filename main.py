import creacion_equipo
import random

print('\nHola entrenador, preparate para combatir!\n')
print('Pokemon disponibles:')
creacion_equipo.mostrar_disponibles()
print()

#Pedimos al jugador que seleccione su equipo:
__equipo = creacion_equipo.seleccionar_pokemon_jugador()
__equipo_rival = creacion_equipo.seleccionar_pokemon_rival()
__jugador = creacion_equipo.Entrenador(__equipo[0], __equipo[1], __equipo[2])
__rival = creacion_equipo.Entrenador(__equipo_rival[0], __equipo_rival[1], __equipo_rival[2])

#Se crea el combate:
combate = creacion_equipo.Combate(__jugador, __rival)
print('COMIENZA EL COMBATE!')
print(f'Rival envia a {combate.get_rival().pokemon_actual().get_nombre()} | PS:{combate.get_rival().pokemon_actual().get_vida()}')
print(f'Tu envias a {combate.get_jugador().pokemon_actual().get_nombre()} | PS:{combate.get_jugador().pokemon_actual().get_vida()}')
print()

#Se inicia el combate:
while not combate.get_terminado():
    combate.siguiente_turno()
