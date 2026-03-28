try:
    with open("dados1.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except FileNotFoundError as error:
    print(f"Erro: Arquivo não encontrado {error}")

finally:
    print("O programa foi executado ate o final")