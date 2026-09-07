class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def __str__(self):
        return f"{super().__str__()} (Elétrico - {self.autonomia_bateria} km)"

# Teste com print chamando o __str__ automaticamente
c1 = Carro("Ford", "Mustang")
c2 = CarroEletrico("BYD", "Seal", 520)

print(c1)
print(c2)