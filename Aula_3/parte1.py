# Abrir um arquivo e saber nome, modo, e se está aberto ou fechado
arquivo = open("arquivo.txt")
print("Arquivo aberto", arquivo)
print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)

# Ler o que está dentro do arquivo
print(arquivo.read())

# Voltar o cursor para o inicio do arquivo
print(arquivo.seek(0))

# Ler apenas 8 caracteres do arquivo
print(arquivo.read(8))

# Fechar um arquivo
arquivo.close()

# Saber se está aberto ou fechado
print(arquivo.closed)
