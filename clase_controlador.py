from clase_modelo import Modelo
from clase_disenio import Vista
class Controlador:
    __modelo: object
    __vista: object
    def __init__(self):
        self.__modelo = Modelo()
        self.__vista = Vista(self)