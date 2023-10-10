import sqlite3
import validate_email as ve

def verificarEmail(email):
    if ve.validate_email(email):
            return True
    else:
        return False

conexao = sqlite3.connect('users.db')

cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    cpf VARCHAR PRIMARY KEY,
                    nome TEXT,
                    email TEXT,
                    senha TEXT
                  )''')

def verificarCpfUser(cpf):
    conexao = sqlite3.connect('users.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT cpf FROM usuarios WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado is None:
        return False 
    else:
        return True 

def verificarInfosUser(cpf,nome,email):
        conexao = sqlite3.connect('users.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT cpf,nome,email FROM usuarios WHERE cpf = ?", (cpf,))
        resultado = cursor.fetchone()
        conexao.close()
        nomeSalvo = resultado[1]
        emailSalvo = resultado[2]
        if nome == nomeSalvo and email == emailSalvo:
            return True
        else:
            return False

def redefinirSenhaUser(cpf, nova_senha):
    conexao = sqlite3.connect('users.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET senha = ? WHERE cpf = ?", (nova_senha, cpf))
    conexao.commit()
    conexao.close()


def adicionaUsuario(cpf, nome, email, senha):
    conexao = sqlite3.connect('users.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)", (cpf, nome, email, senha))
    conexao.commit()
    conexao.close()

def verificaSenha(cpf, senha):
    conexao = sqlite3.connect('users.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        return None
    else:
        senhaSalva = resultado[0]
        if senha == senhaSalva:
            return True
        else:
            return False

def consultar_usuarios():
    conexao = sqlite3.connect('users.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios
#print(consultar_usuarios())

def excluir_usuario(cpf):
    conexao = sqlite3.connect('users.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE cpf = ?", (cpf,))
    conexao.commit()
    conexao.close()

def dropUsers():
    conexao = sqlite3.connect('users.db')
    cursor = conexao.cursor()
    cursor.execute("DROP TABLE usuarios")
    conexao.commit()
    conexao.close()
#dropUsers()

conexao.commit()
conexao.close()


conexao = sqlite3.connect('admin.db')

cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS administradores (
                    cpf VARCHAR PRIMARY KEY,
                    nome TEXT,
                    email TEXT,
                    senha TEXT
                  )''')

def verificarCpfAdmin(cpf):
    conexao = sqlite3.connect('admin.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT cpf FROM administradores WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado is None:
        return False 
    else:
        return True 

def verificarInfosAdmin(cpf,nome,email):
        conexao = sqlite3.connect('admin.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT cpf,nome,email FROM administradores WHERE cpf = ?", (cpf,))
        resultado = cursor.fetchone()
        conexao.close()
        nomeSalvo = resultado[1]
        emailSalvo = resultado[2]
        if nome == nomeSalvo and email == emailSalvo:
            return True
        else:
            return False

def adicionarAdm(cpf,nome,email,senha):
    conexao = sqlite3.connect('admin.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO administradores VALUES (?, ?, ?, ?)", (cpf, nome, email, senha))
    conexao.commit()
    conexao.close()

def verificarAdm(cpf):
    conexao = sqlite3.connect('admin.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT cpf FROM administradores WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado is None:
        return False 
    else:
        return True 

def logarAdm(cpf, senha):
    conexao = sqlite3.connect('admin.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT senha FROM administradores WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado is None:
        return None
    else:
        senhaSalva = resultado[0]
        if senha == senhaSalva:
            return True
        else:
            return False

def redefinirSenhaAdmin(cpf, nova_senha):
    conexao = sqlite3.connect('admin.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE administradores SET senha = ? WHERE cpf = ?", (nova_senha, cpf))
    conexao.commit()
    conexao.close()

def consultar_administradores():
    conexao = sqlite3.connect('admin.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM administradores")
    adminitradores = cursor.fetchall()
    conexao.close()
    return adminitradores


def excluir_administradores(cpf):
    conexao = sqlite3.connect('admin.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM administradores WHERE cpf = ?", (cpf,))
    conexao.commit()
    conexao.close()

conexao.commit()
conexao.close()