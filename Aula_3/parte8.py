with open("arquivo_rad04.txt", "r") as arquivo:
    print("Representação original da minha linha")
    for linha in arquivo:
        dado_da_linha = linha.strip() # .strip() remove o \n da memoria apenas
        print(repr(linha)) # repr() Mostra tudo que o python está lendo 
        print(repr(dado_da_linha))


lista_de_comida = ["pizza", "feijao", "carne", "banana"]
lista_ = ", ".join(lista_de_comida) # "".join() pega a lista e coloca em um unica frase na mesma linha

with open("lista_de_comida.txt", "w") as arquivo:
    arquivo.write(lista_)