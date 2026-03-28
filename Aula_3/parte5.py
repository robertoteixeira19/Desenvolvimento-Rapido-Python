arquivo = open("musica.txt", "r") # Abrir um arquivo e ler
tipos = arquivo.readlines() # Ler todas as linhas e retorna uma lista
print(tipos)
tipos.append("\nLambada") # Adiciona arquivo na lista 
arquivo = open("musica.txt", "w")
arquivo.writelines(tipos)
arquivo.close() # Fechar o arquivo pois não foi escrito com with