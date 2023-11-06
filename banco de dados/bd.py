import mysql.connector


con=mysql.connector.connect(
host='10.28.0.230',
database='cadastro',
user='suporte',
password='suporte')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao banco de dados = ", db_info)

consulta_sql = "select * from cidade"
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("numero total de registros retornardos", cursor.rowcount)




    
#comando = "INSERT INTO cidade(id_cidade, cidade) VALUES (136, 'brasil');"
#cursor.execute(comando)
#con.commit()

#comando = ("DELETE from cidade where cidade = 'brasil'")
#cursor.execute(comando)
#con.commit()


print("mostrandos registros")
for linha in linhas:
    print("cidade =", linha[1])



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão encerrada")