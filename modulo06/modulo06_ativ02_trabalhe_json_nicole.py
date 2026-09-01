import json
# 1. Definição do nome do arquivo que será criado
nome_arquivo = "clientes_nomes.json"


# 2. Dicionário/Lista com os dados dos clientes
# Em vez de strings simples (como no TXT), aqui usamos uma lista de dicionários.
# Isso estrutura melhor os dados, associando chaves (como "Nome completo") aos seus respectivos valores.
clientes = [
    {
        "Nome completo": "Ivan Silva",
        "idade": "40 anos",
        "CEP": "02899-000",
        "ResgMatr": "947541",
        "E-Mail": "ivanpaulino@mail.com"
    },
    {
        "Nome completo": "Beatriz Vitoria",
        "idade": "30 anos",
        "CEP": "057193-000",
        "ResgMatr": "978786",
        "E-Mail": "beavitoria@mail.com"
    },
    {
        "Nome completo": "Eric Renan",
        "idade": "17 anos",
        "CEP": "089880-100",
        "ResgMatr": "98799",
        "E-Mail": "ericrenan@gmail.com"
    }
]

# 3. Bloco de ESCRITA (Salvar) no formato JSON
# O modo "w" abre (ou cria) o arquivo para escrita.
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
# 'json.dump' pega a variável 'clientes' (Python) e a converte para o formato JSON no arquivo.
    # 'ensure_ascii=False' garante que caracteres com acento não sejam desconfigurados.
    # 'indent=2' organiza o arquivo com uma indentação de 2 espaços, tornando-o fácil de ler para humanos (pretty-print).
    json.dump(clientes, arquivo, ensure_ascii=False, indent=2)
print(f"✅ Dados salvos em '{nome_arquivo}' com sucesso!")

# 4. Bloco de LEITURA (Carregar) do arquivo JSON
print("\n--- Carregando dados do arquivo JSON ---")
# O modo "r" abre o arquivo apenas para leitura.
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    clientes_carregados = json.load(arquivo)
# 5. Iterando (percorrendo) os dados carregados
# Como 'clientes_carregados' é uma lista de dicionários, podemos usar um loop 'for' para acessar as informações específicas.
for cliente in clientes_carregados:
    # Acessa os valores informando a chave correspondente entre colchetes, ex: cliente['Nome completo']
    print(f"Cliente: {cliente['Nome completo']} | E-Mail: {cliente['E-Mail']}")