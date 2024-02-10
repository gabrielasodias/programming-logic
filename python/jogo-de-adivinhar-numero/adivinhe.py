import random

print('\nVamos testar a sua sorte!\nAcerte o número\n')

continuar = "SIM"  #Variável para ser utizada no laço de repetição
numeros = [33, 15, 6, 78, 30, 19, 53, 98, 1, 8, 45]  #Lista numérica

#Laço de repetição
while continuar == "SIM":
    sorte_num = random.choice(numeros)  #Sorteia aleatóriamente um número da lista

    print(numeros)
    escolha = int(input('\nEscolha e digite um dos números acima: '))  #Entrada do número de escolha do usuário
    if escolha == sorte_num:  #Se o número escolhido pelo usuário for o mesmo gerado aleatóriamente
        print(f'\nVocê acertou, parabéns! O número que o bot escolheu também é {sorte_num}. Que sorte a sua!')
    else: #Se for contrário à primeira condição
        print(f'\nQue pena. O número que o bot escolheu é {sorte_num}. Não foi dessa vez!')
        print('ATENÇÃO: Lembre-se de digitar um dos números acima. Se o número digitado não estiver na lista, você não tem chance de ganhar.')

    continuar = input('\nDeseja continuar? SIM/NÃO: \n') #Para continuar ou encerrar o laço de repetição
    continuar = continuar.upper() #Caso o 'SIM' seja escrito em letra minúscula. O método upper() formata o texto para maiúsculas

