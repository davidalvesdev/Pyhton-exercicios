# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice
# de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2


if imc < 18.5:
    print('Seu IMC é de {:.2f} e você esta abaixo do peso!'.format(imc))
elif 18.5 <= imc < 25:
   print('Seu IMC é de {:.2f} e você esta no peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f} e você esta com Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de  {:.2f} e você esta com obesidade'.format(imc))
elif imc >= 40:
    print('Seu IMC é de {:.2f} e você esta com Obesidade Mórbida'.format(imc))