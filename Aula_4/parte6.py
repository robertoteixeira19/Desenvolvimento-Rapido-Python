try:
    with open("arquivo_teste.txt", "w") as arquivo:
        arquivo.write("Teste")
        # arquivo_ler = arquivo.read()
        # print(arquivo_ler)

except PermissionError:
    print("Erro: Voce nao tem permissao para alterar o arquivo")
