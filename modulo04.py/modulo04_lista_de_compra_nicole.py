


lista_de_compras = []


while True:


    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")


    print("3. Ver lista")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ").strip()

    if opcao == '1':
        item = input("Digite o nome do item: ").strip().capitalize()
        if item:
            lista_de_compras.append(item)
            print(f"✅ '{item}' adicionado com sucesso!")
        else:
            print("⚠️ O nome do item não pode ser vazio.")

    elif opcao == '2':
        item = input("Digite o nome do item para remover: ").strip().capitalize()
        if item in lista_de_compras:
            lista_de_compras.remove(item)



            print(f"🗑️ '{item}' removido da lista.")
        else:
            print(f"❌ '{item}' não foi encontrado na lista.")



    elif opcao == '3':
        if lista_de_compras:
            print("\n🛒 Sua Lista Atual:")
            for indice, item in enumerate(lista_de_compras, start=1):




                print(f"{indice}. {item}")
        else:
            print("📝 A lista está vazia.")

    elif opcao == '4':
        print("👋 Programa encerrado!")
        break



    else:

        print("🚫 Opção inválida. Digite um número de 1 a 4.")