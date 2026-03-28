# Criar um arquivo pelo codigo
with open("teste1.txt", "w+") as arquivo:
    # Escrever dentro do arquivo criado
    arquivo.write("Iai galerinha blz? \n")
    arquivo.write("Bem vindo turma a minha quinta-feira ")
    
    # Para ler no terminal é necessario voltar o ponteiro para o inicio
    arquivo.seek(0)

    # Para ler o arquivo e retornar (arquivo.read())
    conteudo = arquivo.read()

    print(conteudo)

# Criando uma lista
precos = [200, 100, 300, 500, 400, 600]

# Sobrescrever em um arquivo ja existente usa a letra 'w' para adicionar mais usa a letra 'a'
with open("teste1.txt", "a") as arquuivo:
    # Interar a lista com um laço de repetição
    for preco in precos:
        # Str usado para converter os numeros em strings
        arquivo.wwrite(str(preco) + "\n")

