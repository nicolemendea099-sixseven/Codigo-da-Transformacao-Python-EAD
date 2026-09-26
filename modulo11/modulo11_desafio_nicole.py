import sqlite3

def conectar_banco():
    """Conecta ao banco de dados de tarefas."""
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    """Cria a tabela de tarefas se não existir."""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    """)
    conn.commit()
    conn.close()

def adicionar_tarefa(descricao):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    conn.close()
    print(f"Tarefa '{descricao}' adicionada!")

def listar_tarefas():
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
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    print(f"Tarefa ID {id_tarefa} excluída!")

if __name__ == "__main__":
    criar_tabela()

    # Demonstração
    adicionar_tarefa("Estudar comandos SQL em Python")
    adicionar_tarefa("Finalizar o projeto do módulo")

    listar_tarefas()

    excluir_tarefa(1)

    listar_tarefas()