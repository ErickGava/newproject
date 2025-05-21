import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("bancodedados2")
    return conexao


def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       titulo TEXT, numero_livro TEXT, ano_publicacao INTEGER)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos
                   (nome TEXT PRIMARY KEY, email TEXT, senha, CPF, livros_emprestados TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimo
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_livro TEXT,
                   numero_livro TEXT, data_emprestimo TEXT, data_devolucao TEXT, nome_aluno TEXT)''')
    conexao.commit()
    conexao.close()

def criar_aluno():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute

def criar_livros(titulo, numero_livro, ano_publicacao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO livros (titulo, numero_livro, ano_publicacao) VALUES (?,?,?)''', (titulo, numero_livro, ano_publicacao))
    conexao.commit()
    cursor.close()
    return True

def mostrar_livros(id, titulo, numero_livro, ano_publicacao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM livros""",(id, titulo, numero_livro, ano_publicacao))
    conexao.commit()
    livros = cursor.fetchall()
    cursor.close()
    return livros

def editar_livros(titulo, numero_livro, ano_publicacao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''UPDATE livros SET titulo = ?, numero_livro = ?, ano_publicacao = ? WHERE id = ?''', (titulo, numero_livro, ano_publicacao))
    conexao.commit()
    cursor.close()
    return True

def excluir_livros(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM livro WHERE id = ?''', (id,))
    conexao.commit()
    return True

def emprestar_livro(nome_livro, numero_livro, data_emprestimo, data_devolucao, nome_aluno):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO emprestimo (nome_livro, numero_livro, data_emprestimo, data_devolucao, nome_aluno)
                   VALUES (?,?,?,?,?)''', (nome_livro, numero_livro, data_emprestimo, data_devolucao, nome_aluno) )
    conexao.commit()
    return True

def dados_emprestimo(nome_aluno):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM emprestimo WHERE nome_aluno = ?''', (nome_aluno,))
    conexao.commit()
    return True

def devolver_livro(nome_livro, numero_livro, nome_aluno):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM livros where nome_aluno = ?''', (nome_aluno,))

def livros_aluno():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM emprestimo""")

if __name__ == '__main__':
    criar_tabelas()
    print("Hello World!")
    criar_livros("Testedolivro", "123456679ii", 2005)
    emprestar_livro("peixinho do mar", "123009ia", "01/01/1001", "01/02/1001", "Erick")
    editar_livros("aventuras do senai", "0000", "01/05/5000")