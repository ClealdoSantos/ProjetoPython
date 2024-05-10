from random import randint
numeros =(randint(1, 10), randint(1, 10), randint(1, 10),
            randint(1, 10), randint(1, 10))
print('O valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ',end='')
print(f'\nO Maior valor sorteado foi \033[36m{max(numeros)}\033[m')
print(f'O Menor valor sorteado foi \033[36m{min(numeros)}\033[m')
