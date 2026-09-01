'''




'''
# 1 . Criando um arquivo TXT com o nome "nome_arquivo.txt" 
# e escrevendo algumas informações nele.
# Definição do nome do arquivo que será criado/manipulado
nome_arquivo = "dados_arquivo.txt"


# 2 . Conteúdo a ser escrito no arquivo,definição dos dados que serão salvos
#Os dados estão organizados em uma strings, onde cada item representa uma
# --- ESCRITA ---
conteudo = [
    "Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com\n",
    "Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com\n",
    "Eric Renan;17 anos;089880-100;98799;ericrenan@gmail.com\n"
]


# 3 . Escrevendo no arquivo
# O gerenciador de contexto 'with' garante que o arquivo seja fechado automaticamente após o uso
# 'encoding="utf-8"' garante o suporte correto a acentos e caracteres especiais.
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(conteudo)
print(f"✅ Arquivo '{nome_arquivo}' criado e escrito com sucesso!")



# 4 . Lendo o conteúdo do arquivo
# O modo "r" (read) abre o arquivo apenas para leitura.
# --- LEITURA ---
print("\n--- Lendo o conteúdo do arquivo TXT ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
# O método 'read()' lê todo o conteúdo do arquivo e o armazena como uma única string na variável 'texto'
    texto = arquivo.read()
# Exibe o conteúdo lido diretamente no terminal
    print(texto)