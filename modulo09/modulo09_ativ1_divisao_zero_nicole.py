def calculadora(n1, n2, operacao):
    """
    Função para realizar operações matemáticas básicas com tratamento de erros.
    
    Parâmetros:
    - n1 (float/int): O primeiro número da operação.
    - n2 (float/int): O segundo número da operação.
    - operacao (str): O símbolo da operação ('+', '-', '*', '/').
    
    Retorna:
    - str: Mensagem formatada com o resultado ou o erro capturado.
    """
    try:
        # Valida se os argumentos passados são realmente numéricos
        if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
            raise TypeError("Os valores informados devem ser numéricos.")

        # Executa a operação matemática correspondente
        if operacao == '+':
            resultado = n1 + n2
        elif operacao == '-':
            resultado = n1 - n2
        elif operacao == '*':
            resultado = n1 * n2
        elif operacao == '/':
            resultado = n1 / n2  # Pode gerar ZeroDivisionError se n2 for 0
        else:
            raise ValueError(f"Operação '{operacao}' é inválida. Use '+', '-', '*' ou '/'.")

        return f"Resultado ({n1} {operacao} {n2}): {resultado}"

    except ZeroDivisionError:
        return "Erro: Não é possível realizar divisão por zero!"
    except (TypeError, ValueError) as e:
        return f"Erro de Validação: {e}"


# ==========================================
# TESTES E EXECUÇÃO
# ==========================================

# Teste 1: Divisão normal e outras operações
print("--- Teste 1: Operações Válidas ---")
print(calculadora(10, 2, '/'))
print(calculadora(5, 3, '+'))
print(calculadora(4, 2.5, '*'))

# Teste 2: Tentativa de divisão por zero
print("\n--- Teste 2: Divisão por Zero ---")
print(calculadora(10, 0, '/'))

# Teste 3: Operador inválido
print("\n--- Teste 3: Operador Não Suportado ---")
print(calculadora(10, 2, '^'))

# Teste 4: Entrada com tipo inválido
print("\n--- Teste 4: Tipos de Dados Incorretos ---")
print(calculadora("10", 2, '+'))