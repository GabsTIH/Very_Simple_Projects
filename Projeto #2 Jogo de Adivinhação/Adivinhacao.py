import random
nome = input("Digite o seu nome: ")
def menu():
    choose = int(input(f'''Bem-vindo {nome}!, o que deseja fazer ?
                1 - Jogar
                2 - Dificuldade
                3 - Sair
'''))
    if choose == 1:
        game(a=0, b=10)
    elif choose == 2:
        dificuldade = dif()
        game(a=dificuldade[0], b=dificuldade[1])
    elif choose == 3:
        print("Até uma outra hora!")

def game(a, b):
    number = random.randint(a, b)
    print(f"Psst, o número é {number}")
    lives = 3
    print(f"Estou pensando em um número de {a} até {b}...poderia adivinhar ?")
    while lives > 0:
        tent = int(input(f'''Você tem {lives} tentativas restantes
Digite o seu palpite agora: '''))
        
        if tent == number:
            print("Parabéns! Você acertou")
            break
        else:
            print("Uh oh! Tente novamente! -1 Tentativa")
            lives -= 1

    if lives == 0:
        chance = input("Quer jogar novamente ? S/N: ")
        if chance.upper() == "S":
            menu()
        else:
            print("Até alguma outra hora !")

def dif():
    Easy = [0, 10]
    Medium = [0, 50]
    Hard = [0, 100]
    choice = int(input('''Por favor escolha a dificuldade:
                   1 - Easy
                   2 - Medium
                   3 - Hard
'''))
    if choice == 1:
        print("Dificuldade escolhida: Easy")
        return Easy
    elif choice == 2:
        print("Dificuldade escolhida: Medium")
        return Medium
    elif choice == 3:
        print("Dificuldade escolhida: Hard")
        return Hard
    else:
        print("Opção inválida, escolhendo Easy por padrão.")
        return Easy


menu()