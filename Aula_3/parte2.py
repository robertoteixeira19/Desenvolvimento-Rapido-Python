# Pratica correta para abrir arquivo, pois já vem fechado
with open("arquivo.txt") as arquivo:
    print(arquivo.read())
