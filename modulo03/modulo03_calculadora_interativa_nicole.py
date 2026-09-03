"""
Desafio Extra: Crie um menu interativo de calculadora! 
Use um loop while para que o usuário possa escolher entre 
Soma, Subtração e Sair, repetindo a operação até que ele decida parar.
"""

import time

while True:
    print("\n" + "✨" * 15)
    print(" 🤖 CALCULADORA CABULOSA 🤖 ")
    print("✨" * 15)
    print("1️⃣ - Somar (Juntar as forças)")
    print("2️⃣ - Subtrair (Sumir com a diferença)")
    print("3️⃣ - Sair (Fugir dos números)")
    
    opcao = input("\nQual é a boa de hoje? (1-3): ")
    
    if opcao == "3":
        print("\nDesligando os circuitos... Até a próxima! 👋🤖")
        break
        
    if opcao in ("1", "2"):
        try:
            num1 = float(input("👉 Digite o 1º número: "))
            num2 = float(input("👉 Digite o 2º número: "))
        except ValueError:
            print("\n🚨 Ops! Isso não é um número válido. Tente de novo!")
            continue
            
        print("\nProcessando com inteligência artificial suprema...", end="")
        time.sleep(0.8) # Faz uma pausa dramática para o resultado
        
        if opcao == "1":
            print(f"\n🎉 BOOM! Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcao == "2":
            print(f"\n🎉 BOOM! Resultado: {num1} - {num2} = {num1 - num2}")
    else:
        print("\n🤔 Ih, digitou errado! Escolha apenas 1, 2 ou 3.")