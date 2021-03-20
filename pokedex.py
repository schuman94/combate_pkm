from pokemon import Pokemon
from movimientos import *

class Vaporeon(Pokemon):
    def __init__(self, owner):
                                # PS, ATQ, DEF, VEL
        super().__init__(Agua(), 464, 350, 317, 251, owner=owner)
        self.set_nombre('vaporeon')
        self.set_movimientos(Hidrobomba(), Rayo_hielo(), Golpe_cuerpo(), Escaldar())

class Flareon(Pokemon):
    def __init__(self, owner):
                                 # PS, ATQ, DEF, VEL
        super().__init__(Fuego(), 334, 394, 350, 251, owner=owner)
        self.set_nombre('flareon')
        self.set_movimientos(Llamarada(), Lanzallamas(), Golpe_cuerpo(), Doble_patada())

class Jolteon(Pokemon):
    def __init__(self, owner):
                                     # PS, ATQ, DEF, VEL
        super().__init__(Electrico(), 334, 350, 317, 394, owner=owner)
        self.set_nombre('jolteon')
        self.set_movimientos(Rayo(), Trueno(), Vozarron(), Doble_patada())

class Eevee(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__(Normal(), 314, 229, 251, 229, owner=owner)
        self.set_nombre('eevee')
        self.set_movimientos(Golpe_cuerpo(), Vozarron(), Doble_patada(), Placaje())

class Muk(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__(Veneno(), 414, 339, 328, 218, owner=owner)
        self.set_nombre('muk')
        self.set_movimientos(Bomba_lodo(), Lanzamugre(), Rayo(), Golpe_cuerpo())

class Snorlax(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__(Normal(), 524, 350, 350, 174, owner=owner)
        self.set_nombre('snorlax')
        self.set_movimientos(Golpe_cuerpo(), Terremoto(), Vozarron(), Surf())

class Rattata(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__(Normal(), 264, 232, 185, 267, owner=owner)
        self.set_nombre('rattata')
        self.set_movimientos(Golpe_cuerpo(), Placaje(), Rayo_hielo(), Rayo())

class Tangela(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__(Planta(), 334, 328, 361, 240, owner=owner)
        self.set_nombre('tangela')
        self.set_movimientos(Golpe_cuerpo(), Bomba_germen(), Energibola(), Latigazo())
