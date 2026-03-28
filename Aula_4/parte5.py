import os

try:
    os.remove("dados1.txt")
    print("Arquivo removido com sucesso!")

except FileNotFoundError as erro:
    print("Arquivo nao existe")
    print(f"Descricao do nosso erro {erro}")

except PermissionError:
    print("Sem permissao")

except Exception as e:
    print(f"Erro: {e}")

