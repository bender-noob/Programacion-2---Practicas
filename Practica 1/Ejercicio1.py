# PROGRAMACION 2
# EJERCICIO 1: ECUACION LINEAL
import math

class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def getX(self):
        if self.tieneSolucion():
            return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return None

    def getY(self):
        if self.tieneSolucion():
            return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return None

def main():
    datos = input("Ingrese a, b, c, d, e, f separados por espacios: ").split()
    a, b, c, d, e, f = map(float, datos)

    ecuacion = EcuacionLineal(a, b, c, d, e, f)

    if ecuacion.tieneSolucion():
        print(f"x = {ecuacion.getX():.1f}, y = {ecuacion.getY():.1f}")
    else:
        print("La ecuación no tiene solución")
if __name__ == "__main__":
    main()
