from pokemon import Pokemon

class Entrenador:
    def __init__(self, nombre, pk1: Pokemon, pk2: Pokemon, pk3: Pokemon):
        self.__nombre = nombre
        self.__asignar_pokemones(pk1, pk2, pk3)
        self.__actual = pk1

    def get_nombre(self):
        return self.__nombre

    def __asignar_pokemones(self, pk1, pk2, pk3):
        """Mete en el equipo del entrenador los 3 pokemon indicados"""
        self.__equipo = {}
        self.__equipo[pk1.get_nombre()] = pk1
        self.__equipo[pk2.get_nombre()] = pk2
        self.__equipo[pk3.get_nombre()] = pk3

    def get_pokemon(self, nombre):
        """Devuelve el pokemon seleccionado"""
        return self.__equipo[nombre]

    def pokemon_actual(self):
        """Devuelve el pokemon que se encuentra en combate"""
        return self.__actual

    def eliminar_pokemon_actual(self):
        """Elimina el pokemon actual"""
        self.__actual = None

    def cambiar(self, nombre):
        """Cambia el pokemon que se encuentra en combate por otro seleccionado"""
        try:
            if self.pokemon_actual() == self.get_pokemon(nombre):
                raise ValueError(f'{str(self.get_pokemon(nombre)).upper()} ya se encuentra en combate')
            self.__actual = self.get_pokemon(nombre)
            print(f'{self.get_nombre()} envia a {str(self.get_pokemon(nombre))}!\n')
        except KeyError:
           raise ValueError('El pokemon no se encuentra en el equipo')

    def get_equipo(self):
        """Devuelve un diccionario con el equipo pokemon"""
        return self.__equipo

    def equipo(self):
        """Imprime en la salida los pokemon del equipo"""
        print()
        for i in self.get_equipo().values():
            print(str(i) + ' | PS:' + str(i.get_vida()))
        print()

    def eliminar_pokemon(self, pokemon):
        """Elimina un pokemon del equipo"""
        del self.get_equipo()[pokemon.get_nombre()]
