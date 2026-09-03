usuarios = {
    "admin": "admin123",
    "joao": "senha123",
    "maria": "abc456"
}

def validar_login(usuario, senha):
    return usuarios.get(usuario) == senha

tentativas = 3

while tentativas > 0:
    print("\n--- AUTENTICAÇÃO DE USUÁRIO ---")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if validar_login(usuario, senha):
        print(f"\n🎉 Acesso concedido! Bem-vindo(a), {usuario}!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"❌ Credenciais incorretas. Tentativas restantes: {tentativas}")
        else:
            print("🔒 Acesso bloqueado devido ao excesso de tentativas incorretas.")
