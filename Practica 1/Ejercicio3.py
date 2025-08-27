# PROGRAMACION 2
# EJERCICIO 3: ESTADISTICAS

import math

class Estadisticas:

    @staticmethod
    def promedio(valores):
        return sum(valores) / len(valores)

    @staticmethod
    def desviacion(valores):
        prom = Estadisticas.promedio(valores)
        suma = sum((x - prom) ** 2 for x in valores)
        return math.sqrt(suma / (len(valores) - 1))

def main():
    numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

    if len(numeros) != 10:
        print("Error: Debe ingresar exactamente 10 números.")
        return

    prom = Estadisticas.promedio(numeros)
    desv = Estadisticas.desviacion(numeros)

    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estandar es {desv:.5f}")

if __name__ == "__main__":
    main()
