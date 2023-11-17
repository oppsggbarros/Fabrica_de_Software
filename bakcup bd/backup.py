import mysql.connector

# Conectar ao banco de dados MySQL
with mysql.connector.connect(
    host='10.28.0.230',
    database='back_up',
    user='suporte',
    password='suporte'
) as conexao:
    with conexao.cursor() as cursor:
        if conexao.is_connected():
            db_info = conexao.get_server_info()
            print("Conectado ao banco de dados =", db_info)

        def cadastrar_usuario(nome, email, numero, rg, sexo):
            try:
                cursor.execute("INSERT INTO usuarios_backup (nome, email, numero, rg, sexo) VALUES (%s, %s, %s, %s, %s)", (nome, email, numero, rg, sexo))
                conexao.commit()
                print("Usuário cadastrado com sucesso!")
            except Exception as e:
                print(f"Erro ao cadastrar usuário: {e}")
                conexao.rollback()

        def listar_usuarios():
            try:
                cursor.execute("SELECT * FROM usuarios_backup")
                usuarios = cursor.fetchall()

                for usuario in usuarios:
                    print(usuario)
            except Exception as e:
                print(f"Erro ao listar usuários: {e}")

        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        numero = input("Digite seu número de celular: ")
        rg = input("Digite seu RG: ")
        sexo = input("Digite seu sexo: ")

        cadastrar_usuario(nome, email, numero, rg, sexo)

        print("\nLista de Usuários:")
        listar_usuarios()
