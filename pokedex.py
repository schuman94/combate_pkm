from pokemon import Pokemon
from movimientos import *

class Vaporeon(Pokemon):
    def __init__(self):
                                # PS, ATQ, DEF, VEL
        super().__init__('agua', 464, 319, 219, 229)
        self.set_nombre('vaporeon')
        self.set_movimientos(Hidrobomba(), Surf(), Golpe_cuerpo(), Escaldar())

class Flareon(Pokemon):
    def __init__(self):
                                # PS, ATQ, DEF, VEL
        super().__init__('fuego', 334, 359, 219, 229)
        self.set_nombre('flareon')
        self.set_movimientos(Llamarada(), Lanzallamas(), Golpe_cuerpo(), Malicioso())

class Jolteon(Pokemon):
    def __init__(self):
                                     # PS, ATQ, DEF, VEL
        super().__init__('electrico', 334, 287, 219, 359)
        self.set_nombre('jolteon')
        self.set_movimientos(Rayo(), Trueno(), Vozarron(), Onda_trueno())

class Eevee(Pokemon):
    def __init__(self):
                                  # PS, ATQ, DEF, VEL
        super().__init__('normal', 314, 229, 218, 229)
        self.set_nombre('eevee')
        self.set_movimientos(Golpe_cuerpo(), Vozarron(), Onda_trueno(), Malicioso())
