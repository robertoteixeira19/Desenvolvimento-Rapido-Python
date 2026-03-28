lista = [1, 2, 3, 4, 5, 6, 7]

try:
    posicao = int(input("Digite uma posição da lista: "))
    print(lista[posicao])

except IndexError:
    print("Posição não existe")

except ValueError:
    print("Digite um numero valido")
