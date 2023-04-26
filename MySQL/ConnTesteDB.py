#Install MySql

#CREATE DATABASE db_Alunos;

#pip3 install mysql-connector-python


import mysql.connector


con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='Princesspeach@me2')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")