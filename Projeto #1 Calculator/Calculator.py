#Calculadora by GabsTIH
nome = input("Digite o seu nome: ")
#Pergunta o nome ao usuário para lhe dar uma mensagem de boas-vindas
print(f'Bem-vindo à calculadora, {nome} !')

def menu():
#Pede ao usuário qual é a operação que ele precisa realizar
    Escolha = int(input('''
O que deseja fazer hoje ?
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    5 - Sair
'''))
#Árvore de escolhas
    if Escolha == 1:
        somar()
    elif Escolha == 2:
        sub()
    elif Escolha == 3:
        multi()
    elif Escolha == 4:
        divi()
    elif Escolha == 5:
        print("Até a próxima então!")


def somar():
    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))
    print(number1,"+",number2,"=",number1+number2)
    reset()

def sub():
    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))
    print(number1,"-",number2,"=",number1-number2)
    reset()

def multi():
    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))
    print(number1,"x",number2,"=",number1*number2)
    reset()

def divi():
    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))
    print(number1,"/",number2,"=",number1/number2)
    reset()

def reset():
    choice = input("Deseja fazer outra operação? S/N ")
    if choice == "S" or choice == "s":
        menu()
    else:
        print(f' Até mais! {nome}')

menu()