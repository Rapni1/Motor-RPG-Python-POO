class Personaje():
    def __init__(self, nombre, vida_maxima, ataque, defensa):
        self.nombre = nombre
        self.vida = vida_maxima
        self.ataque = ataque
        self.defensa = defensa
        self.inventario = Inventario()
    def atacar(self, objetivo):
        daño_real = self.ataque - objetivo.defensa
        objetivo.vida = objetivo.vida - daño_real
        print(f"¡{self.nombre} ataca a {objetivo.nombre} por {daño_real} de daño!")
        print(f"A {objetivo.nombre} le quedan {objetivo.vida} HP")
    def usar_pocion(self):
        if len(self.inventario.bolsa) > 0:
            pocion_activa = self.inventario.bolsa.pop(0)
            self.vida = self.vida + pocion_activa.poder_curacion
            print(f"{self.nombre} bebio {pocion_activa.nombre}")
            print(f"Recupero {pocion_activa.poder_curacion} HP, Vida actual: {self.vida} HP.")
        else:
            print(f"{self.nombre} rebusca en su inventario pero no le quedan mas pociones.")
class Mago(Personaje):
    def __init__(self, nombre, vida_maxima, ataque, defensa, mana):
        super().__init__(nombre, vida_maxima, ataque, defensa)
        self.mana = mana
        
    def curar(self):
        if self.mana >= 10:
            self.vida = self.vida + 20
            self.mana = self.mana - 10
            print(f"{self.nombre} se ha curado 20 HP! Ahora tiene {self.vida} HP")
        else:
            print(f"¡{self.nombre} no tiene mana suficiente para curarse")
    def atacar(self, objetivo):
        if self.mana >= 5:
            self.mana = self.mana - 5
            objetivo.vida = objetivo.vida - self.ataque
            print(f"El mago {self.nombre} utilizo el hechizo bola de fuego contra un {objetivo.nombre}, Le quedan {self.mana} puntos de mana")
        else:
            print(f"El mago {self.nombre} tiene {self.mana} puntos de mana, No puede atacar")

class Pocion:
    def __init__(self, nombre, poder_curacion):
        self.nombre = nombre
        self.poder_curacion = poder_curacion

class Inventario:
    def __init__(self):
        self.bolsa = []
    def agregar(self, item):
        self.bolsa.append(item)
        print(f"{item.nombre} añadido en el inventario.")
    def mostrar(self):
        print("\n--- Inventario ---")
        if len(self.bolsa) == 0:
            print("El inventario esta vacio")
        else:
            for item in self.bolsa:
                print(f" {item.nombre} (Cura {item.poder_curacion} HP)")
        print("------------------")
        
jugador = Personaje("Rapni", 100, 40, 16)
aliado = Mago("Merlin", 70, 15, 5, 30)
enemigo = Personaje("Lobo", 60, 20, 10)
pocion_menor = Pocion("Pocion menor", 20)
pocion_mayor = Pocion("Pocion mayor", 50)
jugador.inventario.agregar(pocion_menor)
enemigo.atacar(jugador)
jugador.inventario.mostrar()
jugador.usar_pocion()
jugador.usar_pocion()
jugador.inventario.mostrar()




        