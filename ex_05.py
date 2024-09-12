# Write a program that plays "stone, paper or scissors" against the user. The game must continue until the user chooses to stop, and returns the number of wins from the user, the machine, and draws.

import random

def det_resultado(usuario, computador):
   regra = [['e', 'c', 'v'],  # Pedra contra [pedra, papel, tesoura]
            ['v', 'e', 'c'],  # Papel contra [pedra, papel, tesoura]
            ['c', 'v', 'e']]  # Tesoura contra [pedra, papel, tesoura]
   return regra[usuario][computador]

opcao_jogo = {1: 'pedra', 2: 'papel', 3: 'tesoura'}

pont_comp = 0
pont_usua = 0
empat = 0

while True:
   print("""
   Escolha uma opção:
   [1] - Pedra
   [2] - Papel
   [3] - Tesoura
   [4] - Sair
   """)

   usuario = input('Sua jogada: ')

   if usuario.isdigit():
       usuario = int(usuario)
       if 1 <= usuario <= 4:
           if usuario == 4:
               print(f'Número de Empates: {empat}')
               print(f'Vitórias do Computador: {pont_comp}')
               print(f'Suas Vitórias: {pont_usua}')
               break
           computador = random.choice(range(1, 3))
           usuario_escolhido = opcao_jogo[usuario]
           computador_escolhido = opcao_jogo[computador]

           print(f"Você escolheu {usuario_escolhido} e o computador escolheu {computador_escolhido}.")

           resultado = det_resultado(usuario - 1, computador - 1)

           if resultado == 'e':
               empat += 1
               print('EMPATE')
           elif resultado == 'v':
               pont_usua += 1
               print('VOCÊ venceu!')
           elif resultado == 'c':
               pont_comp += 1
               print('COMPUTADOR venceu!')
       else:
           print("Opção inválida. Escolha um número entre 1 e 4.")
   else:
       print("Entrada inválida. Digite um número.")
