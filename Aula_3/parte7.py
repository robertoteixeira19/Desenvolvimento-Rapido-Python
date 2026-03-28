disciplinas = ["rad\n", "poo\n", "disp movel\n"] # Criar uma lista com 3 disciplinas 

with open ("disciplinas_fav.txt", "w") as arquivo: # Criar um arquivo
    arquivo.write("minhas disciplinas + top \n") # Escrever dentro do arquivo criado
    arquivo.writelines(disciplinas) # Escrever dentro do arquivo criado

with open("disciplinas_fav.txt", "r") as arquivo: # Abrindo arquivo modo leitura
    print(arquivo.read()) # Printando o arquivo no terminal