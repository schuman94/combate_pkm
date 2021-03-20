from tipos import *


class Movimiento:
    def __init__(self, nombre, tipo: Tipo(), pp, potencia, precision, efecto):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__pp = pp
        self.__potencia = potencia
        self.__precision = precision
        self.__efecto = efecto

    def get_nombre(self):
        return self.__nombre

    def get_pp(self):
        return self.__pp

    def reducir_pp(self):
        """Reduce los pp en 1"""
        self.__pp -= 1

    def get_potencia(self):
        return self.__potencia

    def get_precision(self):
        return self.__precision

    def get_efecto(self):
        return self.__efecto

    def get_tipo(self):
        return self.__tipo

    def usar(self):
        """Gasta un pp del ataque"""
        if self.get_pp() < 1:
            raise ValueError('No quedan PPs')
        else:
            self.reducir_pp()

    def __str__(self):
        return self.get_nombre().upper() + ' | PP: ' + str(self.get_pp())


class Hidrobomba(Movimiento):
    def __init__(self):
                                             # PP Pot  Prec Ef
        super().__init__('hidrobomba', Agua(), 5, 110, 80, None)


class Surf(Movimiento):
    def __init__(self):
                                       # PP Pot Prec  Ef
        super().__init__('surf', Agua(), 15, 90, 100, None)


class Golpe_cuerpo(Movimiento):
    def __init__(self):
                                                 # PP Pot Prec  Ef
        super().__init__('golpe cuerpo', Normal(), 15, 85, 100, 'paralizar')


class Escaldar(Movimiento):
    def __init__(self):
                                           # PP Pot Prec  Ef
        super().__init__('escaldar', Agua(), 15, 80, 100, 'quemar')


class Lanzallamas(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('lanzallamas', Fuego(), 15, 90, 100, 'quemar')


class Llamarada(Movimiento):
    def __init__(self):
                                             # PP Pot Prec  Ef
        super().__init__('llamarada', Fuego(), 5, 110, 85, 'quemar')


class Malicioso(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('malicioso', Normal(), 30, 0, 100, 'reducir_defensa')


class Rayo(Movimiento):
    def __init__(self):
                                            # PP Pot Prec  Ef
        super().__init__('rayo', Electrico(), 15, 90, 100, 'paralizar')


class Trueno(Movimiento):
    def __init__(self):
                                              # PP  Pot Prec  Ef
        super().__init__('trueno', Electrico(), 10, 110, 70, 'paralizar')


class Onda_trueno(Movimiento):
    def __init__(self):
                                                   # PP Pot Prec  Ef
        super().__init__('onda trueno', Electrico(), 20, 0, 90, 'paralizar')


class Vozarron(Movimiento):
    def __init__(self):
                                             # PP Pot Prec  Ef
        super().__init__('vozarron', Normal(), 10, 90, 100, None)


class Terremoto(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('terremoto', Tierra(), 10, 100, 100, None)


class Tierra_viva(Movimiento):
    def __init__(self):
                                                # PP Pot Prec  Ef
        super().__init__('tierra viva', Tierra(), 10, 90, 100, None)


class Doble_patada(Movimiento):
    def __init__(self):
                                                # PP Pot Prec  Ef
        super().__init__('doble patada', Lucha(), 30, 60, 100, None)

class Placaje(Movimiento):
    def __init__(self):
                                             # PP Pot Prec  Ef
        super().__init__('placaje', Normal(), 35, 40, 100, None)

class Rayo_hielo(Movimiento):
    def __init__(self):
                                              # PP Pot Prec  Ef
        super().__init__('rayo hielo', Hielo(), 10, 90, 100, 'congelar')

class Bomba_germen(Movimiento):
    def __init__(self):
                                                 # PP Pot Prec  Ef
        super().__init__('bomba germen', Planta(), 15, 80, 100, None)

class Energibola(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('energibola', Planta(), 10, 90, 100, None)

class Latigazo(Movimiento):
    def __init__(self):
                                             # PP Pot Prec  Ef
        super().__init__('latigazo', Planta(), 10, 120, 85, None)

class Lanzamugre(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('lanzamugre', Veneno(), 5, 120, 80, 'Envenenar')

class Bomba_lodo(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('bomba lodo', Veneno(), 10, 90, 100, 'Envenenar')

#SERGIO CHULIAN MANTEL
