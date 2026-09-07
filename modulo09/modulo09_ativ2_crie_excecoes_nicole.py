# ==========================================
# 1. Definição da Exceção Personalizada
# ==========================================
class SaldoInsuficienteError(Exception):
    """Exceção personalizada lançada quando o saque excede o saldo disponível."""
    pass


# ==========================================
# 2. Definição da Classe da Conta Bancária
# ==========================================
class ContaBancaria:
    def __init__(self, saldo_inicial=0.0):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.saldo = float(saldo_inicial)

    def depositar(self, valor):
        """Adiciona saldo à conta após validar se o valor é positivo."""
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self.saldo += valor
        return f"Depósito de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.saldo:.2f}"

    def sacar(self, valor):
        """Realiza um saque validando valor positivo e saldo suficiente."""
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        
        if valor > self.saldo:
            raise SaldoInsuficienteError(
                f"Saque negado! Valor solicitado: R$ {valor:.2f} | Saldo disponível: R$ {self.saldo:.2f}"
            )
        
        self.saldo -= valor
        return f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo restante: R$ {self.saldo:.2f}"


# ==========================================
# 3. Testes e Execução do Código
# ==========================================
if __name__ == "__main__":
    minha_conta = ContaBancaria(saldo_inicial=100.0)

    # Teste 1: Saque permitido
    print("--- Teste 1: Saque Permitido ---")
    try:
        print(minha_conta.sacar(40.0))
    except (SaldoInsuficienteError, ValueError) as erro:
        print(f"Erro: {erro}")

    # Teste 2: Saque negado por saldo insuficiente
    print("\n--- Teste 2: Saque Sem Saldo ---")
    try:
        print(minha_conta.sacar(100.0))
    except (SaldoInsuficienteError, ValueError) as erro:
        print(f"Erro capturado: {erro}")

    # Teste 3: Tentativa de sacar valor negativo ou zero
    print("\n--- Teste 3: Valor Inválido ---")
    try:
        print(minha_conta.sacar(-15.0))
    except (SaldoInsuficienteError, ValueError) as erro:
        print(f"Erro capturado: {erro}")