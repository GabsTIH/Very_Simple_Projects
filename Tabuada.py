#Tabuada by Gabs
def menu():
    Escolha = input('''Qual tipo de tabuada deseja?
                    Digite 1 para tabuadas do 1 a 10
                    Digite 2 para tabuadas da sua escolha
                    ''')
#Pede ao usuário qual tipo de tabuada ele deseja, se é uma tabuada comum do 1 a 10, ou se deseja fazer uma personalizada
    if Escolha == "1":
        tabuadaS()
    else:
        tabuadaP()
#Caso o usuário escolha a tabuada do 1 a 10, o programa executará uma tabela predefinida
#Caso contrário, executará o programa de tabuada personalizada

def tabuadaS():
    for i in (1,2,3,4,5,6,7,8,9,10):
        print("Tabuada do", i)
        for x in (1,2,3,4,5,6,7,8,9,10):
            print(i,"x",x, "=", i*x)

def tabuadaP():
    escNum = int(input("Digite o número que deseja multiplicar: "))
    escVorS = input('''Deseja que ele se multiplique somente uma vez, ou várias vezes ?
                    Digite 1 para uma vez
                    Digite 2 para múltiplas vezes
                    ''')

    if escVorS == "1":
        escNumDos = int(input("Digite o número que deseja multiplicar pelo escolhido anteriormente: "))
        print(escNum, "x", escNumDos, "=", escNum * escNumDos)
    elif escVorS == "2":
        escMin = int(input("Digite de que número a tabuada deve começar: "))
        escMax = int(input("Agora, digite o número que a tabuada deve terminar: "))
        sequen = range(escMin, escMax + 1)
        sequen_list = list(sequen)
        for i in sequen_list:
            print(escNum, "x", i, "=", escNum * i)

menu()