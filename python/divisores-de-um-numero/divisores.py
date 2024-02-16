print('\nDivisores de um número')

#Tratamento de exceção
try:
    numero = int(input('Digite um número inteiro: ')) #Entrada de um número inteiro
    lista_range = list(range(1,numero+1)) #Cria uma lista com uma sequência baseada no número digitado

    divisor_list = [] #Lista para os divisores

    for i in lista_range: #Passa por todos os elementos da lista
      if numero%i == 0: #Verifica se é um divisor
        divisor_list.append(i) #Se for divisor, acrescenta na lista divisor_list

    print('\nOs divisores são: ')
    print(divisor_list) #Exibe a lista de divisores

except: #Caso não seja digitado um número inteiro
   print('\nDigite apenas números inteiros.\n')