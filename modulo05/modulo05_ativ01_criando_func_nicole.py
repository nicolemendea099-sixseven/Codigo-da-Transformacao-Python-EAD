from typing import List, Tuple

# Base de dados para autenticação
USUARIOS = {
    "admin": "1234",
    "ana": "senha123",
    "carlos": "python2026"
}

def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada formatada."""
    nome_limpo = nome.strip().title()
    return f"Olá, {nome_limpo if nome_limpo else 'Visitante'}! Seja bem-vindo(a) ao sistema."

def calcular_media(notas: List[float]) -> Tuple[float, str]:
    """Calcula a média de uma lista de notas e define o status de aprovação."""
    if not notas:
        return 0.0, "Sem notas"
    
    media = sum(notas) / len(notas)
    situacao = "APROVADO" if media >= 7.0 else "REPROVADO"
    return round(media, 2), situacao

def maior_menor(numeros: List[float]) -> Tuple[float, float]:
    """Encontra e retorna o maior e o menor valor de uma lista numérica."""
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return max(numeros), min(numeros)

def validar_login(usuario: str, senha: str) -> bool:
    """Autentica o usuário comparando as credenciais no dicionário."""
    usuario_limpo = usuario.strip().lower()
    return USUARIOS.get(usuario_limpo) == senha

def executar_sistema():
    print("=" * 40)
    print("       SISTEMA MULTIFUNCIONAL")
    print("=" * 40)
    
    # Módulo de Autenticação
    user = input("Usuário: ")
    password = input("Senha: ")
    
    if not validar_login(user, password):
        print("\n❌ Falha na autenticação: Credenciais inválidas.")
        return

    # Mensagem de Boas-Vindas
    print(f"\n✅ {saudacao(user)}")
    
    # Módulo 1: Média Escolar
    print("\n[ 1. Análise de Desempenho Escolar ]")
    try:
        e_notas = input("Digite as notas separadas por espaço (ex: 8.5 7.0 9.0): ")
        lista_notas = [float(n) for n in e_notas.split()]
        media, status = calcular_media(lista_notas)
        print(f"📊 Média Final: {media} | Status: {status}")
    except ValueError:
        print("⚠️ Formato de nota inválido. Digite apenas números.")

    # Módulo 2: Análise Numérica
    print("\n[ 2. Identificador de Maior/Menor Valor ]")
    try:
        e_nums = input("Digite números inteiros ou decimais (ex: 12 5 99 3): ")
        lista_nums = [float(n) for n in e_nums.split()]
        maior, menor = maior_menor(lista_nums)
        print(f"📈 Maior Valor: {maior}")
        print(f"📉 Menor Valor: {menor}")
    except ValueError as e:
        print(f"⚠️ Erro ao processar os números: {e}")

if __name__ == "__main__":
    executar_sistema()