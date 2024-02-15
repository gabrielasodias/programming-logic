print('\nIMC')
print('\nOBS: Utilize ponto (.) ao invés de virgula (,) para números decimais.\n')
peso = float(input('Digite seu peso: ')) #Entrada do peso
altura = float(input('Digite sua altura: ')) #Entrada da altura

imc = peso / altura **2 #Fórmula para calcular o imc

print(f'\nSeu IMC é: {imc:,.1f}') #imc exibido com formatação de uma casa decimal
print('Sua classificação é: ')
#Classificações de acordo com a tabela de imc
if imc < 18.5:
    print('Magreza.')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal.')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso. Obesidade grau I.')
elif imc >= 30.0 and imc <= 39.9:
    print('Obesidade. Obesidade grau II.')
else:
    print('Obesidade grave. Obesidade grau III.')
