import random

print('\nVamos testar a sua sorte!\nAcerte o número\n')

continuar = "SIM"
numeros = [33, 15, 6, 78, 30, 19, 53, 98, 1, 8, 45]

#Laço de repetição
while continuar == "SIM":
    sorte_num = random.choice(numeros)

    print(numeros)
    escolha = int(input('\nEscolha e digite um dos números acima: '))
    if escolha == sorte_num:
        print(f'\nVocê acertou, parabéns! O número que o bot escolheu também é {sorte_num}. Que sorte a sua!')
    else:
        print(f'\nQue pena. O número que o bot escolheu é {sorte_num}. Não foi dessa vez!')
        print('ATENÇÃO: Lembre-se de digitar um dos números acima. Se o número digitado não estiver na lista, você não tem chance de ganhar.')

    continuar = input('\nDeseja continuar? SIM/NÃO: \n') 
    continuar = continuar.upper()
