# EJERCICIO 2 - EXAMEN PARCIAL 2

class Persona:
    def __init__(self, nombre: str, edad: int, peso: float):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

class Cabina:
    def __init__(self, nroCabina: int):
        self.nroCabina = nroCabina
        self.personasAbordo = []  # PERSONA

    def agregarPersona(self, p: Persona):
        # MAXIMO 10 PERSONAS
        if len(self.personasAbordo) >= 10:
            return False, "La cabina ya tiene 10 personas."

        # NO SUPERAR LOS 50KG POR CABINA
        peso_actual = sum(persona.peso for persona in self.personasAbordo)
        if peso_actual + p.peso > 50:
            return False, "El peso maximo de 50 kg sería superado."

        self.personasAbordo.append(p)
        return True, "Persona Agregada Correctamente :D"

class Linea:
    def __init__(self, color: str):
        self.color = color
        self.cabinas = []  # CABINA

    def agregarCabina(self, nroCabina: int):
        nueva = Cabina(nroCabina)
        self.cabinas.append(nueva)

    def agregarPersona(self, p: Persona, nroCabina: int):
        for cabina in self.cabinas:
            if cabina.nroCabina == nroCabina:
                return cabina.agregarPersona(p)
        return False, "No existe la cabina indicada :("

    def ingresoTotal(self):
        total = 0
        for cabina in self.cabinas:
            for persona in cabina.personasAbordo:
                if persona.edad < 25 or persona.edad > 60:
                    total += 1.5        # TAR PREFERENCIAL
                else:
                    total += 3          # TAR REGULAR
        return total

class MiTeleferico:
    def __init__(self):
        self.lineas = []            # LINEA
        self.cantidadIngresos = 0.0

    def agregarLinea(self, color: str):
        nueva = Linea(color)
        self.lineas.append(nueva)

    def agregarPersona(self, p: Persona, colorLinea: str, nroCabina: int):
        for linea in self.lineas:
            if linea.color == colorLinea:
                ok, msg = linea.agregarPersona(p, nroCabina)
                return ok, msg
        return False, "No existe la linea indicada :("

    def calcularIngresoTotal(self):
        total = 0
        for linea in self.lineas:
            total += linea.ingresoTotal()
        self.cantidadIngresos = total
        return total

    def lineaMayorIngreso(self):
        if not self.lineas:
            return None

        ingresos_por_linea = [(linea.color, linea.ingresoTotal()) for linea in self.lineas]
        ingresos_por_linea.sort(key=lambda x: x[1], reverse=True)
        
        mayor = ingresos_por_linea[0]
        return mayor
