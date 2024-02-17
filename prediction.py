import random
import time
secretNumber = random.randint(0, 100)
winner = 0
print('INICIANDO...')
time.sleep(1)
print(f'{"JOGO DA ADIVINHAÇÃO":=^40}')
print(f'{"ESCOLHA UM NÚMERO E TENTE GANHAR DE MIM!":=^40}')
print(f'{"VOCÊ TEM 5 TENTATIVAS":^40}')
print(f'{'':=^40}')
resposta = int(input('Escolha um número de 0 a 100: '))
if winner == 0:
    if secretNumber % 2 == 0:
        print('DICA: é um número PAR!')
    else:
        print('DICA: é um número IMPAR!')
    for c in range(0, 4):

        if resposta > secretNumber:
            print('DICA: Tente um valor menor!')
        if resposta < secretNumber:
            print('DICA: Tente um valor maior!')
        if resposta == secretNumber:
            winner = 1
            break
        resposta = int(input('Tente novamente: '))
if winner == 1:
    print('Parabéns!!! Você ganhou!!!')
else:
    print('Que pena, talvez na próxima!')
