from pokemon import Pokemon
from movimientos import *

class Vaporeon(Pokemon):
    def __init__(self, owner):
                                # PS, ATQ, DEF, VEL
        super().__init__('agua', 464, 350, 317, 251, owner=owner)
        self.set_nombre('vaporeon')
        self.set_movimientos(Hidrobomba(), Rayo_hielo(), Golpe_cuerpo(), Escaldar())

class Flareon(Pokemon):
    def __init__(self, owner):
                                 # PS, ATQ, DEF, VEL
        super().__init__('fuego', 334, 394, 350, 251, owner=owner)
        self.set_nombre('flareon')
        self.set_movimientos(Llamarada(), Lanzallamas(), Golpe_cuerpo(), Doble_patada())

class Jolteon(Pokemon):
    def __init__(self, owner):
                                     # PS, ATQ, DEF, VEL
        super().__init__('electrico', 334, 350, 317, 394, owner=owner)
        self.set_nombre('jolteon')
        self.set_movimientos(Rayo(), Trueno(), Vozarron(), Doble_patada())

class Eevee(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__('normal', 314, 229, 251, 229, owner=owner)
        self.set_nombre('eevee')
        self.set_movimientos(Golpe_cuerpo(), Vozarron(), Doble_patada(), Placaje())

class Marowak(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__('tierra', 324, 284, 350, 207, owner=owner)
        self.set_nombre('marowak')
        self.set_movimientos(Golpe_cuerpo(), Vozarron(), Terremoto(), Tierra_viva())

class Snorlax(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__('normal', 524, 350, 350, 174, owner=owner)
        self.set_nombre('snorlax')
        self.set_movimientos(Golpe_cuerpo(), Terremoto(), Vozarron(), Surf())

class Rattata(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__('normal', 264, 232, 185, 267, owner=owner)
        self.set_nombre('rattata')
        self.set_movimientos(Golpe_cuerpo(), Placaje(), Rayo_hielo(), Rayo())

class Tangela(Pokemon):
    def __init__(self, owner):
                                  # PS, ATQ, DEF, VEL
        super().__init__('planta', 334, 328, 361, 240, owner=owner)
        self.set_nombre('tangela')
        self.set_movimientos(Golpe_cuerpo(), Bomba_germen(), Energibola(), Latigazo())
