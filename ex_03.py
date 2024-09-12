# Write a program that prints the first 10 numbers of the Fibonacci sequence.

def fibonacci(numero):
   if numero == 0 or numero == 1:
       return numero
   elif numero == 1 or numero == 2:
       return numero
   else:
       return (fibonacci(numero-1) + fibonacci(numero-2))
for i in range(10):
   print(fibonacci(i))
