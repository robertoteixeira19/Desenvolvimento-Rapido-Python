usuario = "user"
password = "pass123"

try:
    user = input("Usuario: ")
    senha = input("Senha: ")

    if user != usuario:
        raise Exception ("Usuário incorreto")    
    if senha != password:
        raise Exception("Senha incorreta")
    print("Login realizado com sucesso")

except Exception as erro:
    print(f"Erro: {erro}")