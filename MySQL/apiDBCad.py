#Criar Tabela
#CREATE DATABASE db_Alunos; 
#USE db_Alunos;
#CREATE TABLE tb_aluno (
#    name VARCHAR(20),
#    sobrenome VARCHAR(20),
#   turma VARCHAR(20)
#);
#INSERT INTO tb_aluno(name, sobrenome, turma)values ('xxxx', 'yyyy', 'A');


import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='Princesspeach@me2')
    cursor = con.cursor()
    sql = "INSERT INTO tb_aluno (name, sobrenome,turma) VALUES (%s, %s, %s)"
    val = ("Joao Antonio", "da Silva", "API e Micro")
    cursor.execute(sql, val)
    con.commit()
    print("\nCadastrado com Sucesso")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")