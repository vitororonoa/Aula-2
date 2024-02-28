print('Hello players')

import random

n = [3,2,1]
for c in n:
    randomico = random.randint(1,5)
    jogador1 = int(input('Digite seu numero player 1>>'))
    jogador2 = int(input('Digite seu numero player2>>'))
    c = c - 1
    if randomico == jogador1:
        print(f'parabens (p1) você acertou  o numero é: {randomico}')
        break

    elif randomico != jogador1 and randomico > 0:
       print(f'você errou (p1), o numero é: {randomico}, você tem apenas {c} chances')
       if c == 0:
           print(f'você esgotou as possibilidades, total de chances >> {c}')
           break
        
    if randomico == jogador2:
         print(f'parabens (p2) você acertou, o numero é: {randomico}')
         break

    elif randomico != jogador2 and randomico > 0:
        print(f'você errou (p2), o numero é: {randomico}, você tem apenas {c} chances')
        if c == 0:
           print(f'você esgotou as possibilidades, total de chances >> {c}')
           break
        
    
