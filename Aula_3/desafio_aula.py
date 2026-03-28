
disciplinas = ["dev python", "dev c++", "banco de dados"]

with open("disciplinas.txt", "w") as arquivo:  
    arquivo.write("Minhas 3 disciplinas favoritas \n") 
    for i, d in enumerate(disciplinas, 1): 
       arquivo.write(f'{i}. {d}\n')

with open("disciplinas.txt", "r") as arquivo: 
    print(arquivo.read()) 
