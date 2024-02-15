print('\nIMC')
print('\nOBS: Utilize ponto (.) ao invés de virgula (,) para números decimais.\n')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura **2

print(f'\nSeu IMC é: {imc:,.1f}')
print('Sua classificação é: ')
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
