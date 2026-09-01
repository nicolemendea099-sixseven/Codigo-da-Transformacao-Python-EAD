class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, autonomia_bateria):
        super().__init__(marca, modelo, ano)
        self.autonomia_bateria = autonomia_bateria

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")

meu_carro_eletrico = CarroEletrico("Tesla", "Model S", 2022, 600)
meu_carro_eletrico.exibir_informacoes()
