aluno = {
    "nome": "Ana Silva",
    "idade": 16,
    "turma": "2º Ano B",
    "notas": [8.5, 9.0, 7.5]
}

media = sum(aluno["notas"]) / len(aluno["notas"])
aluno["media"] = round(media, 2)

if media >= 7.0:
    aluno["situação"] = "Aprovado"
elif media >= 5.0:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"

print("=" * 30)
print("      FICHA DO ALUNO")
print("=" * 30)
print(f"Nome:       {aluno['nome']}")
print(f"Idade:      {aluno['idade']} anos")
print(f"Turma:      {aluno['turma']}")
print(f"Notas:      {', '.join(map(str, aluno['notas']))}")
print(f"Média:      {aluno['media']:.2f}")
print(f"Situação:   {aluno['situação']}")
print("=" * 30)