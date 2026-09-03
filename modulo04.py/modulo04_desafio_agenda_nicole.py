agenda = {}

while True:
    print("\n--- MENU DA AGENDA ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Buscar Contato")
    print("4. Ver Todos os Contatos")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ").strip()

    if escolha == '1':
        nome = input("Digite o nome do contato: ").strip().title()
        if nome in agenda:
            print(f"❌ O contato '{nome}' já existe.")
        else:
            telefone = input("Digite o telefone: ").strip()
            email = input("Digite o email: ").strip().lower()
            agenda[nome] = {"telefone": telefone, "email": email}
            print(f"✅ Contato '{nome}' adicionado com sucesso!")

    elif escolha == '2':
        nome = input("Digite o nome do contato para remover: ").strip().title()
        if nome in agenda:
            del agenda[nome]
            print(f"🗑️ Contato '{nome}' removido.")
        else:
            print(f"❌ O contato '{nome}' não foi encontrado.")

    elif escolha == '3':
        nome = input("Digite o nome do contato para buscar: ").strip().title()
        if nome in agenda:
            contato = agenda[nome]
            print(f"\n--- Detalhes: {nome} ---")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email:    {contato['email']}")
        else:
            print(f"❌ O contato '{nome}' não foi encontrado.")

    elif escolha == '4':
        if not agenda:
            print("📝 A agenda está vazia.")
        else:
            print("\n--- Todos os Contatos ---")
            for nome, detalhes in agenda.items():
                print(f"Nome:     {nome}")
                print(f"Telefone: {detalhes['telefone']}")
                print(f"Email:    {detalhes['email']}")
                print("-" * 25)

    elif escolha == '5':
        print("👋 Saindo da agenda. Até mais!")
        break

    else:
        print("🚫 Opção inválida. Digite um número de 1 a 5.")