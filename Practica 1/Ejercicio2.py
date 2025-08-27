# PROGRAMACION 2
# EJERCICIO 2: ECUACION CUADRATICA

import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b**2 - 4 * self.__a * self.__c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b + math.sqrt(d)) / (2 * self.__a)
        else:
            return 0

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b - math.sqrt(d)) / (2 * self.__a)
        else:
            return 0

def main():
    datos = input("Ingrese a, b, c: ").split()
    a, b, c = map(float, datos)

    eq = EcuacionCuadratica(a, b, c)
    d = eq.getDiscriminante()

    if d > 0:
        print(f"La ecuacion tiene dos raices {eq.getRaiz1():.6f} y {eq.getRaiz2():.6f}")
    elif d == 0:
        print(f"La ecuacion tiene una raiz {eq.getRaiz1():.0f}")
    else:
        print("La ecuacion no tiene raices reales")


if __name__ == "__main__":
    main()
