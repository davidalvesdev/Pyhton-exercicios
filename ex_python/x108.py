# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que
# consiga mostrar os números como um valor monetário formatado.
import moeda

num = float(input('Digite um número: '))


print(f'A metade de {moeda.real(num)} é {moeda.real(moeda.metade(num))}')
print(f'O dobro de {moeda.real(num)} é {moeda.real(moeda.dobro(num))}')
print(f'Aumentando 10% temos {moeda.real(moeda.aumento(num))}')
print(f'Diminuindo 13% temos {moeda.real(moeda.diminuir(num))}')