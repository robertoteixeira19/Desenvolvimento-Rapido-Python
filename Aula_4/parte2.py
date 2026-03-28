try:
    numero = int(input("Digite um numero: "))
    resultado = 20/numero
    print(resultado)

except ValueError:
    print("Erro: Deve ser digitado um numero inteiro")

except ZeroDivisionError:
    print("Erro: O numero da divisao eigual a 0, digite um numero diferente")

except Exception as erro:
    print(f"Erro inesperado: {erro}")