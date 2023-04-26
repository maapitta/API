#Criar Tabela
#INstall MYSQL
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

    consulta_sql = "select * from tb_aluno"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)
    print("\nMostrando os autores cadastrados")
    for linha in linhas:
        print("Nome:", linha[0])
        print("Sobrenome:", linha[1])
        print("Turma:", linha[2], "\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")