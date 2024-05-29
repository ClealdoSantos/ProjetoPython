valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('_*' * 30 )
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')