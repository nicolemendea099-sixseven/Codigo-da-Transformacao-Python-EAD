import csv
# 1. Definição do nome do arquivo e das colunas (cabeçalho)
nome_arquivo = "notas_alunos.csv"
campos = ["Aluno", "Materia", "Nota"]

# --- ADICIONAR E SALVAR NOTAS ---
notas = [
    {"Aluno": "Ivan Silva", "Materia": "Matemática", "Nota": 9.5},
    {"Aluno": "Beatriz Vitoria", "Materia": "Portugues", "Nota": 10.0},
    {"Aluno": "Eric Renan", "Materia": "Educação fisica", "Nota": 8.5}
]

# Usa utf-8-sig para garantir total compatibilidade de acentos no Excel
# 2. Dados a serem inseridos
# --- ADICIONAR E SALVAR NOTAS ---
# Assim como no JSON, estamos usando uma lista de dicionários. 
# As chaves dos dicionários devem ser exatamente iguais aos nomes definidos na lista 'campos' acima.
with open(nome_arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:
# 'csv.DictWriter' é a ferramenta que sabe como pegar nossos dicionários e transformá-los em linhas de CSV.
    # Precisamos informar o arquivo e quais são as colunas (fieldnames).
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerows(clientes_notas := notas)

print(f"✅ Notas salvas no arquivo '{nome_arquivo}'!")

# --- CARREGAR E EXIBIR NOTAS ---
print("\n--- Lendo o arquivo CSV de Notas ---")
with open(nome_arquivo, "r", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Aluno: {linha['Aluno']} | Matéria: {linha['Materia']} | Nota: {linha['Nota']}")