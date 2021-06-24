class personaje:
    def __init__(self):
        self.nombre=""#input("Ingrese el nombre de su personaje... ")
        self.edad=24

        self.saludFisica=0
        self.saludMetal=0
        self.sueldo=0
        self.carisma=0


class actividades:
    def __init__(self):
        self.nombre=""
        self.salubridad=0
        self.puntos=[]

class trabajo:
    def __init__(self):
        self.nombre=""
        self.salubridad=0

class comida:
    def __init__(self):
        self.nombre=""
        self.saludable=0