soma = 0
cont = 0
for c in range( 1, 7):
    num = int(input('Digite o {}º valor:'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou \033[4;35m{}\033[m números PARES e a soma foi \033[4;31m{}\033[m'.format(cont, soma))
