num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('_*' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores \033[36mPARES\033[m digitados foram: {num[0]}')
print(f'Os valores \033[36mIMPARES\033[m digitados foram: {num[1]}')
