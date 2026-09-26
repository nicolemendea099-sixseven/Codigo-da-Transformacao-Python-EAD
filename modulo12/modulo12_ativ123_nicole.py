import unittest

# 1 e 2: Classe Calculadora com operações básicas
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        # 3: Tratamento de entrada inválida
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b


# Suíte de testes unitários cobrindo as atividades 1, 2 e 3
class TestCalculadora(unittest.TestCase):

    def setUp(self):
        """Instancia a classe Calculadora antes de cada teste."""
        self.calc = Calculadora()

    # Testes da Atividade 1 e 2: Função e métodos de soma/operações
    def test_somar_positivos(self):
        self.assertEqual(self.calc.somar(2, 3), 5)

    def test_somar_negativos(self):
        self.assertEqual(self.calc.somar(-1, -1), -2)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_dividir_valido(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    # Teste da Atividade 3: Validação de exceção para entradas inválidas
    def test_divisao_por_zero_lanca_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()