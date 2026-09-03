"""
Desafio Extra: Crie um menu interativo de calculadora! 
Use um loop while para que o usuário possa escolher entre 
Soma, Subtração e Sair, repetindo a operação até que ele decida parar.
"""

while True:
    print("\n--- CALCULADORA ---")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1-3): ")

    if opcao == "3":
        print("Encerrando a calculadora. Até mais!")
        break
    elif opcao in ("1", "2"):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == "1":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        else:
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")
