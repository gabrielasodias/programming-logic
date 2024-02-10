from math import sqrt #Biblioteca para uso da função

print('\nEquação do Segundo Grau\n')

#Entrada dos valores
a = int (input('Digite o valor de A: '))
b = int (input('Digite o valor de B: '))
c = int (input('Digite o valor de C: '))

delta = b**2 - 4*a*c #Calcula o delta

if delta < 0: #Para delta negativo
    print("Delta negativo")
else: #Calcula as raízes
    raiz_delta = sqrt(delta) 
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
 
    print(f'As raízes são {x1} e {x2}') #Exibi o resultado
