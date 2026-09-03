"""
Classificando idades: Use if-elif-else para criar um programa
que classifique a idade de uma pessoa em 
"Criança", "Adolescente", "Adulto" ou "Idoso".
"""

from datetime import datetime

def mostrar_menu():
    """Exibe as opções do menu para o usuário."""
    print("\n--- Menu de Verificação de Idade ---")
    print("1. Informar Idade, Ano de Nascimento e Classificação")
    print("2. Sair")
    print("------------------------------------")

def obter_idade_atual():
    """Solicita e retorna a idade atual válida do usuário."""
    while True:
        try:
            idade_str = input("Digite sua idade atual: ")
            idade = int(idade_str)
            
            if 0 <= idade <= 120:  # Idade razoável para validação
                return idade
            else:
                print("Idade inválida. Por favor, digite uma idade entre 0 e 120 anos.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

def classificar_idade(idade):
    """Retorna a classificação da faixa etária com base na idade."""
    if idade <= 12:
        return "Criança 🎈"
    elif idade <= 17:
        return "Adolescente 🎧"
    elif idade <= 59:
        return "Adulto 💼"
    else:
        return "Idoso 👑"

def main():
    """Função principal que executa o menu interativo."""
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            idade_atual = obter_idade_atual()
            
            ano_atual = datetime.now().year
            ano_nascimento = ano_atual - idade_atual
            categoria = classificar_idade(idade_atual)

            print(f"\nConsiderando o ano atual ({ano_atual}) e sua idade de {idade_atual} anos:")
            print(f"👉 Ano de nascimento aproximado: {ano_nascimento}")
            print(f"👉 Faixa etária: {categoria}")

            if idade_atual >= 18:
                print("👉 Status: MAIOR de idade")
            else:
                print("👉 Status: MENOR de idade")

        elif escolha == '2':
            print("\nSaindo do programa. Até mais!")
            break  # Sai do loop while
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()