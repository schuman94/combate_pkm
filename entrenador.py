from pokemon import Pokemon

class Entrenador:
    def __init__(self, pk1: Pokemon, pk2: Pokemon, pk3: Pokemon):
        self.__asignar_pokemones(pk1, pk2, pk3)
        self.__actual = pk1

    def __asignar_pokemones(self, pk1, pk2, pk3):
        self.__equipo = {}
        self.__equipo[pk1.get_nombre()] = pk1
        self.__equipo[pk2.get_nombre()] = pk2
        self.__equipo[pk3.get_nombre()] = pk3
    def get_pokemon(self, nombre):
        return self.__equipo[nombre]

    def pokemon(self):
        return self.__actual

    def cambiar(self, nombre):
        try:
            if self.__actual == self.get_pokemon(nombre):
                raise ValueError(f'{str(self.get_pokemon(nombre)).upper()} ya se encuentra en combate')
            self.__actual = self.get_pokemon(nombre)
            print(f'Adelante {str(self.get_pokemon(nombre)).upper()}!')
        except KeyError:
            print('No tienes ese pokemon en tu equipo')

    def equipo(self):
        print()
        for i in self.__equipo.values():
            print(str(i).upper())
        print()
