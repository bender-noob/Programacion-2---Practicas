# PRACTICA 3 - JUEGO 2; HERENCIA
import random
# SUPER CLASE
class Juego:
    def __init__(self, numeroDeVidas: int):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        print("\n🔄 Reiniciando Partida...")
        self.numeroDeVidas_inicial = self.numeroDeVidas
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
        print(f"🏆 Record Actual: {self.record}")
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"❌ Te queda(n) {self.numeroDeVidas} vida(s).")
            return True
        else:
            print("💀 No te quedan mas Vidas.")
            return False
# CLASE HEREDADA
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas: int):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = None
    def validaNumero(self, n: int) -> bool:
        return 0 <= n <= 1
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("🎮 Adivina el numero entre 0 y 10!")
        while True:
            try:
                intento = int(input("👉 Ingresa tu numero: "))
            except ValueError:
                print("⚠️ Ingresa un numero válido.")
                continue
            # VALIDACION NUMERO
            if not self.validaNumero(intento):
                print("⚠️ Numero fuera de rango (0 - 10). Intenta otra vez.")
                continue
            if intento == self.numeroAAdivinar:
                print("🎉 ¡ADIVINASTE!")
                self.actualizaRecord()
                break
            else:
                if intento < self.numeroAAdivinar:
                    print("📉 El numero a adivinar es mayor.")
                else:
                    print("📈 El numero a adivinar es menor.")
                if not self.quitaVida():
                    print(f"😢 Perdiste. El numero era {self.numeroAAdivinar}.")
                    break
# JUEGO ADIVINAR PAR
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n: int) -> bool:
        while self.numeroAAdivinar is not None and self.numeroAAdivinar % 2 != 0:
            self.numeroAAdivinar = random.randint(0, 10)
        if 0 <= n <= 10 and n % 2 == 0:
            return True
        else:
            print("⚠️ El numero ingresado NO es par o esta fuera del rango (0 - 10).")
            return False
# JUEGO ADIVINAR IMPAR
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n: int) -> bool:
        while self.numeroAAdivinar is not None and self.numeroAAdivinar % 2 == 0:
            self.numeroAAdivinar = random.randint(0, 10)
        if 0 <= n <= 10 and n % 2 != 0:
            return True
        else:
            print("⚠️ El numero ingresado NO es impar o esta fuera del rango (0 - 10).")
            return False
# APLICACION
class Aplicacion:
    @staticmethod
    def main():
        print("===== Juego Adivina Numero =====")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()
        print("\n===== Juego Adivina Numero PAR =====")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega()
        print("\n===== Juego Adivina Numero IMPAR =====")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega()
# EJECUTAR
if __name__ == "__main__":
    Aplicacion.main()
