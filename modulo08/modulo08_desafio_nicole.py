class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.historico_emprestimos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo, leitor):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    self.historico_emprestimos.append({"livro": livro.titulo, "leitor": leitor})
                    print(f"Empréstimo de '{livro.titulo}' para {leitor} realizado!")
                    return
                print(f"O livro '{livro.titulo}' já está emprestado.")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def listar_disponiveis(self):
        print(f"\n--- Livros Disponíveis ({self.nome}) ---")
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        for livro in disponiveis:
            print(livro)

    def listar_historico_emprestimos(self):
        print(f"\n--- Histórico de Empréstimos ---")
        for registro in self.historico_emprestimos:
            print(f"Livro: {registro['livro']} | Leitor: {registro['leitor']}")

# Teste
bib = Biblioteca("Biblioteca Central")
bib.adicionar_livro(Livro("1984", "George Orwell"))
bib.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis"))

bib.listar_disponiveis()
bib.emprestar_livro("1984", "Carlos")
bib.listar_disponiveis()
bib.listar_historico_emprestimos()