try:
    with open("novo_arquivo.txt", "w") as arquivo:
        arquivo.write("Escrevendo algo....")
        print("Arquivo criado com sucesso")
except Exception as erro:
    print(f"Erro ao manipular o arquivo{erro}")
finally:
    print("Arquivo fechado")
