num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-*' * 30)
print(f'A lista completa é \033[036m{num}\033[m')
print(f'A lista de PARES é \033[036m{pares}\033[m')
print(f'a lista de IMPARES é \033[036m{impares}\033[m')
