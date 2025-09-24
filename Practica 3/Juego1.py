# PRACTICA 3 - JUEGO 1; HERENCIA
import random
# SUPER CLASE
class Juego:
    def __init__(self, numeroDeVidas: int):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        print("🔄 Reiniciando Partida...")
        self.numeroDeVidas_inicial = self.numeroDeVidas
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
        print(f"🏆 Nuevo Record: {self.record}")
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"❌ Te queda(n) {self.numeroDeVidas} vida(s).")
            return True
        else:
            print("💀 No te quedan mas vidas.")
            return False
# CLASE HEREDADA
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas: int):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = None
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("🎮 Bienvenido al juego: Adivina el numero entre 0 y 10!")
        while True:
            try:
                intento = int(input("👉 INGRESA TU NUMERO: "))
            except ValueError:
                print("⚠️ Por favor ingresa un numero valido.")
                continue
            if intento == self.numeroAAdivinar:
                print("🎉 ¡LO ADIVINASTE!")
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
# APLICACION
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)  # SE INICIA CON 3 VIDAS
        juego.juega()
# EJECUCION DE PROGRAMA
if __name__ == "__main__":
    Aplicacion.main()