class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria  # Autonomia em km

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Autonomia: {self.autonomia_bateria} km")

    def __str__(self):
        return f"{super().__str__()} (Elétrico - Autonomia: {self.autonomia_bateria} km)"


# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla")
meu_eletrico = CarroEletrico("Tesla", "Model 3", 500)

meu_carro.exibir_info()
meu_eletrico.exibir_info()

# Exibição usando o método especial __str__
print(meu_carro)
print(meu_eletrico)