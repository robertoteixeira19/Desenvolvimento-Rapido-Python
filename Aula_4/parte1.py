try:
    resultado = 20/0
    print(resultado)
except ZeroDivisionError as erro:
    print("Erro: Não é possível realizar divisão por 0", erro)
 
 