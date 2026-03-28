try:
    with open("desafio1.txt", "w+") as arquivo:
        arquivo.write("Teste de permissão!")
        arquivo.seek(0)
        print(arquivo.read())
        
except PermissionError:
    print("Sem permissão")
