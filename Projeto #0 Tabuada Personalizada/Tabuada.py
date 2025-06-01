#Tabuada by Gabs
def menu():
    choose = input('''Qual tipo de tabuada deseja?
                    Digite 1 para tabuadas do 1 a 10
                    Digite 2 para tabuadas da sua escolha
                    ''')
#Pede ao usuário qual tipo de tabuada ele deseja, se é uma tabuada comum do 1 a 10, ou se deseja fazer uma personalizada
    if choose == "1":
        tabuadaSimples()
    else:
        tabuadaPersonalizada()
#Caso o usuário escolha a tabuada do 1 a 10, o programa executará uma tabela predefinida
#Caso contrário, executará o programa de tabuada personalizada

def tabuadaSimples():
    'Retorna uma lista de tabuada predefinida do 1 ao 10, Exemplo: 1 x 1 = 1, 1 x 2 = 2, ..., 10 x 10 = 100'
    for i in (1,2,3,4,5,6,7,8,9,10):
        print(f"Tabuada do {i}")
        for x in (1,2,3,4,5,6,7,8,9,10):
            print(f"{i}x{x}={i*x}")

def tabuadaPersonalizada():
    'Permite ao usuário fazer uma tabuada personalizada, colocando o inicio, e o fim'
    escNum = int(input("Digite o número que deseja multiplicar: "))
    #Pede ao usuário o número que ele deseja que a tabuada seja baseada
    escMin = int(input("Digite de que número a tabuada deve começar: "))
    #Pede ao usuário o número em que a tabuada deve começar, e.g. Se o usuário pediu como base o número 5, e o começo dele for 3, a tabuada começara do 5 x 3
    escMax = int(input("Agora, digite o número que a tabuada deve terminar: "))
    #Pede ao usuário o número em que a tabuada deve terminar, e.g. Se o usuário pediu como base 5, começo 3, e como máximo 10, a tabuada será do 5 x 3 até o 5 x 10 
    for i in range(escMin, escMax + 1):
        print(escNum, "x", i, "=", escNum * i)

menu()