def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade tem que ser maior que 0")
    
    elif idade < 18:
        raise ValueError("Idade minima e 18 anos")
    
    return "Acesso permitido"

try:
    idade = int(input("Digite a sua idade: "))
    print(verificar_idade(idade))

except ValueError as erro:
    print((f"Erro: {erro}"))