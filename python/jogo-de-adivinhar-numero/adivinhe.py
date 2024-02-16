import random

print('\nVamos testar a sua sorte!\nAcerte o número\n')

continuar = "SIM"  #Variável para ser utizada no laço de repetição
numeros = ['33', '15', '6', '78', '30', '19', '53', '98', '1', '8', '45']  #Lista de números em formato de string

#Laço de repetição
while continuar == "SIM":
    sorte_num = random.choice(numeros)  #Sorteia aleatóriamente um elemento da lista

    print(numeros)
    escolha = (input('\nEscolha e digite um dos números acima: '))  #Entrada do número de escolha do usuário (armazena como string)
    if escolha == sorte_num:  #Se a entrada do usuário for o mesmo que foi gerado aleatóriamente
        print(f'\nVocê acertou, parabéns! O número que o bot escolheu também é {sorte_num}. Que sorte a sua!')
    else: #Se for contrário à primeira condição
        print(f'\nQue pena. O número que o bot escolheu é {sorte_num}. Não foi dessa vez!')
        print('ATENÇÃO: Lembre-se de digitar um dos números acima. Se o número digitado não estiver na lista, você não tem chance de ganhar.')

    continuar = input('\nDeseja continuar? SIM/NÃO: \n') #Para continuar ou encerrar o laço de repetição
    continuar = continuar.upper() #Caso o 'SIM' seja escrito em letra minúscula. O método upper() formata o texto para maiúsculas

