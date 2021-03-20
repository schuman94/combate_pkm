class Tipo:
    def __init__(self):
        self.__eficaz = []
        self.__no_eficaz = []

    def get_elemento(self):
        return self.__elemento

    def set_elemento(self, elemento):
        self.__elemento = elemento

    def get_eficaz(self):
        """Devuelve una lista con los elementos contra los que es eficaz"""
        return self.__eficaz

    def get_no_eficaz(self):
        """Devuelve una lista con los elementos contra los que no es eficaz"""
        return self.__no_eficaz

    def set_eficaz(self, lista):
        for i in lista:
            super.get_eficaz().append(i)

    def set_no_eficaz(self, lista):
        for i in lista:
            super.get_no_eficaz().append(i)

class Agua(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('agua')
        self.set_eficaz(['fuego', 'tierra'])
        self.set_no_eficaz(['planta', 'agua'])

class Fuego(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('fuego')
        self.set_eficaz(['planta'])
        self.set_no_eficaz(['agua', 'fuego'])

class Electrico(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('electrico')
        self.set_eficaz(['agua'])
        self.set_no_eficaz(['planta', 'electrico', 'tierra'])

class Normal(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('normal')
        self.set_eficaz([])
        self.set_no_eficaz([])

class Veneno(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('veneno')
        self.set_eficaz(['planta'])
        self.set_no_eficaz(['veneno', 'tierra'])

class Planta(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('planta')
        self.set_eficaz(['agua', 'tierra'])
        self.set_no_eficaz(['planta', 'veneno', 'fuego'])

class Hielo(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('hielo')
        self.set_eficaz(['planta', 'tierra'])
        self.set_no_eficaz(['agua', 'fuego', 'hielo'])

class Tierra(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('tierra')
        self.set_eficaz(['electrico', 'veneno', 'fuego'])
        self.set_no_eficaz(['planta'])

class Lucha(Tipo):
    def __init__(self):
        super.__init__()
        self.set_elemento('lucha')
        self.set_eficaz(['normal', 'hielo'])
        self.set_no_eficaz(['veneno'])
