import sqlite3

def conectar_banco():
    """Conecta ao banco de dados SQLite (cria o arquivo se não existir)."""
    return sqlite3.connect("gerenciador.db")

def criar_tabelas():
    """Cria a tabela de clientes e a tabela do desafio extra (tarefas)."""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    # Tabela de Clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    
    # Tabela de Tarefas (Desafio Extra)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    """)
    
    conn.commit()
    conn.close()

# ==========================================
# OPERAÇÕES CRUD - CLIENTES
# ==========================================

def adicionar_cliente(nome, email):
    """Insere um novo cliente no banco de dados."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()
    print(f"Cliente '{nome}' adicionado com sucesso!")

def listar_clientes():
    """Lista todos os clientes cadastrados."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    
    print("\n--- Lista de Clientes ---")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | E-mail: {cliente[2]}")
    print("-------------------------\n")

def atualizar_email_cliente(id_cliente, novo_email):
    """Atualiza o e-mail de um cliente existente."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conn.commit()
    conn.close()
    print(f"E-mail do cliente ID {id_cliente} atualizado com sucesso!")

def excluir_cliente(id_cliente):
    """Exclui um cliente com base no ID."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conn.commit()
    conn.close()
    print(f"Cliente ID {id_cliente} excluído com sucesso!")

# ==========================================
# CONSULTAS AVANÇADAS / FILTROS
# ==========================================

def buscar_clientes_por_inicial(letra):
    """Busca clientes cujo nome começa com a letra especificada."""
    conn = conectar_banco()
    cursor = conn.cursor()
    # Utiliza o operador LIKE com % para buscar pelo início do nome
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", (f"{letra}%",))
    clientes = cursor.fetchall()
    conn.close()
    
    print(f"\n--- Clientes que começam com '{letra}' ---")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | E-mail: {cliente[2]}")
    print("------------------------------------------\n")

# ==========================================
# DESAFIO EXTRA: SISTEMA DE TAREFAS
# ==========================================

def adicionar_tarefa(descricao):
    """Adiciona uma nova tarefa."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    conn.close()
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def listar_tarefas():
    """Visualiza todas as tarefas cadastradas."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    
    print("\n--- Lista de Tarefas ---")
    for tarefa in tarefas:
        print(f"ID: {tarefa[0]} | Descrição: {tarefa[1]} | Status: {tarefa[2]}")
    print("------------------------\n")

def excluir_tarefa(id_tarefa):
    """Exclui uma tarefa com base no ID."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    print(f"Tarefa ID {id_tarefa} excluída com sucesso!")


# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================

if __name__ == "__main__":
    # Inicializa as tabelas
    criar_tabelas()

    # 1. Adicionando Clientes (Create)
    print(">>> Adicionando clientes...")
    adicionar_cliente("Ana Silva", "ana@email.com")
    adicionar_cliente("Arthur Souza", "arthur@email.com")
    adicionar_cliente("Carlos Oliveira", "carlos@email.com")

    # 2. Listando Clientes (Read)
    listar_clientes()

    # 3. Atualizando E-mail (Update)
    print(">>> Atualizando e-mail da Ana...")
    atualizar_email_cliente(1, "ana.silva@novoemail.com")
    listar_clientes()

    # 4. Filtrando dados (Nomes com 'A')
    buscar_clientes_por_inicial("A")

    # 5. Excluindo Cliente (Delete)
    print(">>> Excluindo cliente ID 3...")
    excluir_cliente(3)
    listar_clientes()

    # ------------------------------------------
    # Testando o Desafio Extra (Tarefas)
    # ------------------------------------------
    print("\n==========================================")
    print("    EXECUTANDO DESAFIO EXTRA: TAREFAS     ")
    print("==========================================")
    
    adicionar_tarefa("Estudar comandos SQL em Python")
    adicionar_tarefa("Finalizar o projeto do módulo")
    
    listar_tarefas()
    
    print(">>> Excluindo tarefa ID 1...")
    excluir_tarefa(1)
    
    listar_tarefas()