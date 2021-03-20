from abc import ABC, abstractmethod

class Movimiento:
    def __init__(self, nombre, tipo, pp, potencia, precision, efecto):
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
        super().__init__('hidrobomba', 'agua', 5, 110, 80, None)


class Surf(Movimiento):
    def __init__(self):
                                       # PP Pot Prec  Ef
        super().__init__('surf', 'agua', 15, 90, 100, None)


class Golpe_cuerpo(Movimiento):
    def __init__(self):
                                                 # PP Pot Prec  Ef
        super().__init__('golpe cuerpo', 'normal', 15, 85, 100, 'paralizar')


class Escaldar(Movimiento):
    def __init__(self):
                                           # PP Pot Prec  Ef
        super().__init__('escaldar', 'agua', 15, 80, 100, 'quemar')


class Lanzallamas(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('lanzallamas', 'fuego', 15, 90, 100, 'quemar')


class Llamarada(Movimiento):
    def __init__(self):
                                             # PP Pot Prec  Ef
        super().__init__('llamarada', 'fuego', 5, 110, 85, 'quemar')


class Malicioso(Movimiento):
    def __init__(self):
                                               # PP Pot Prec  Ef
        super().__init__('malicioso', 'normal', 30, 0, 100, 'reducir_defensa')


class Rayo(Movimiento):
    def __init__(self):
                                            # PP Pot Prec  Ef
        super().__init__('rayo', 'electrico', 15, 90, 100, 'paralizar')


class Trueno(Movimiento):
    def __init__(self):
                                              # PP  Pot Prec  Ef
        super().__init__('trueno', 'electrico', 10, 110, 70, 'paralizar')


class Onda_trueno(Movimiento):
    def __init__(self):
                                                   # PP Pot Prec  Ef
        super().__init__('onda trueno', 'electrico', 20, 0, 90, 'paralizar')


class Vozarron(Movimiento):
    def __init__(self):
                                             # PP Pot Prec  Ef
        super().__init__('vozarron', 'normal', 10, 90, 100, None)
