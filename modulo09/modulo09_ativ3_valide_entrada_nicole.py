# ==========================================
# ATIVIDADE 03: Validação de Entrada de Usuário
# ==========================================

def solicitar_idade_valida(idade_minima=1, idade_maxima=120):
    """
    Solicita a idade do usuário e valida se a entrada é um número inteiro válido
    dentro do intervalo especificado.
    
    Parâmetros:
    - idade_minima (int): Idade mínima aceita (padrão: 1).
    - idade_maxima (int): Idade máxima aceita (padrão: 120).
    
    Retorna:
    - int: A idade validada do usuário.
    """
    while True:
        # .strip() remove espaços vazios no início e final da digitação
        entrada = input("Por favor, digite a sua idade: ").strip()
        
        try:
            idade = int(entrada)
            
            # Validação do intervalo esperado
            if idade < idade_minima or idade > idade_maxima:
                print(f"Erro: A idade deve estar entre {idade_minima} e {idade_maxima} anos.\n")
                continue 
            
            return idade

        except ValueError:
            print("Erro: Entrada inválida! Por favor, digite apenas números inteiros.\n")


# ==========================================
# EXECUÇÃO E TESTES DO CÓDIGO
# ==========================================
if __name__ == "__main__":
    print("--- Teste da Atividade 3: Validação de Idade ---\n")
    
    idade_confirmada = solicitar_idade_valida()
    print(f"\nSucesso! Idade de {idade_confirmada} anos registrada no sistema.")