try:
    with open("parte7.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("arquivo lido com sucesso")

except FileNotFoundError:
    print("ERRO: arquivo não encontrado")

else: print(conteudo)

finally:
    print("Finalizado a leitura do arquivo")