"""
Gerador de Boletim Escolar Fictício (versão interativa)
O usuário digita seu próprio nome, idade e telefone fake, além das notas.
Usa datetime para registrar o horário de entrega do boletim.
"""

from datetime import datetime
from faker import Faker

fake = Faker('pt_BR')

NOTA_MINIMA = 6.0

DISCIPLINAS = [
    "Matemática",
    "Português",
    "História",
    "Geografia",
    "Ciências",
    "Inglês",
]


def escolher_nome():
    return input("\nDigite seu nome fake: ").strip()


def escolher_idade():
    while True:
        idade = input("Digite sua idade fake: ").strip()
        if idade.isdigit():
            return idade
        print("Digite um número válido.")


def escolher_telefone():
    return input("Digite seu telefone fake: ").strip()


def digitar_notas():
    """Deixa o usuário digitar a nota de cada disciplina."""
    print("\nAgora digite suas notas (de 0 a 10) para cada disciplina:")
    notas = {}
    for disciplina in DISCIPLINAS:
        while True:
            try:
                nota = float(input(f"  {disciplina}: ").replace(",", "."))
                if 0 <= nota <= 10:
                    notas[disciplina] = round(nota, 1)
                    break
                else:
                    print("  A nota deve estar entre 0 e 10.")
            except ValueError:
                print("  Digite um número válido (ex: 7.5).")
    return notas


def gerar_boletim():
    nome = escolher_nome()
    idade = escolher_idade()
    telefone = escolher_telefone()
    notas = digitar_notas()

    media = round(sum(notas.values()) / len(notas), 2)
    situacao = "APROVADO(A)" if media >= NOTA_MINIMA else "REPROVADO(A)"
    horario_entrega = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "notas": notas,
        "media": media,
        "situacao": situacao,
        "horario_entrega": horario_entrega,
    }


def imprimir_boletim(boletim):
    largura = 45
    print("\n" + "=" * largura)
    print("BOLETIM ESCOLAR".center(largura))
    print("=" * largura)
    print(f"Aluno: {boletim['nome']}")
    print(f"Idade: {boletim['idade']}")
    print(f"Telefone: {boletim['telefone']}")
    print("-" * largura)
    print("Notas por disciplina:")
    for disciplina, nota in boletim["notas"].items():
        print(f"  {disciplina:<15}: {nota}")
    print("-" * largura)
    print(f"Média final: {boletim['media']}")
    print(f"Nota mínima para aprovação: {NOTA_MINIMA}")
    print(f"Situação: {boletim['situacao']}")
    print("-" * largura)
    print(f"Boletim entregue em: {boletim['horario_entrega']}")
    print("=" * largura)


if __name__ == "__main__":
    boletim = gerar_boletim()
    imprimir_boletim(boletim)