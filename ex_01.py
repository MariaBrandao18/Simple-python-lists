#Ask the user to enter a number. If the number is even, display "Even number". If it’s odd, display "Odd number"

numero = int(input('Digite um número: '))
if numero % 2 == 0:
   print ('Número par', '{}'.format(numero))
else:
   print('Número ímpar', '{}'.format(numero))
