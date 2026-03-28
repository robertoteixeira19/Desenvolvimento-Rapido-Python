precos = [200, 300, 400, 1000, 100]

with open("precos_roupas.txt", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + "\n")
        print(preco)
    # Adicionar algo na lista depois do laço for
    arquivo.write("6000" + "\n")
    