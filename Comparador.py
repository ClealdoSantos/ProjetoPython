n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('\033[4;36m O PRIMEIRO valor {} é Maior!\033[m'.format(n1))
elif n2 > n1:
    print('\033[4;31m O SEGUNDO valor {} é maior!\033[m'.format(n2))
else:
    print('\033[4;32m Os dois valores {} e {} são IGUAIS!\033[m'.format( n1, n2))
