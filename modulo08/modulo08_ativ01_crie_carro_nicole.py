class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

# Exemplo de uso da classe Carro
meu_carro = Carro("Volkswagen", "Nivus", 2022)
print(meu_carro.exibir_informacoes())

print("CADASTRO DE CARROS/n")


