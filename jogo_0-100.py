from random import randint
from time import sleep
x = randint(1,101)
t = 1
while True:
    n = int(input('Digite seu palpite de 1 à 100: '))
    sleep(0.5)
    if n < x:
        print('Por favor, pense em um valor MAIOR!')
    if n > x:
        print('Por favor, pense em um valor menor!')
    if n == x:
        break
    t += 1
print(f'Parabéns!!! Você ganhou o jogo com {t} Tentativas!')
sleep(2)