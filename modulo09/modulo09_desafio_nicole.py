class CredenciaisInvalidasError(Exception):
    pass

def sistema_login(usuario_correto="admin", senha_correta="1234", max_tentativas=3):
    tentativas = 0
    
    while tentativas < max_tentativas:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        try:
            if usuario != usuario_correto or senha != senha_correta:
                raise CredenciaisInvalidasError("Usuário ou senha incorretos.")
            print("\nLogin realizado com sucesso!")
            return True
        except CredenciaisInvalidasError as e:
            tentativas += 1
            restantes = max_tentativas - tentativas
            print(f"{e} Tentativas restantes: {restantes}\n")
            
    print("Conta bloqueada temporariamente devido ao excesso de tentativas falhas.")
    return False

# Exemplo de uso
sistema_login()