resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
             maior = núm
        if núm < menor:
             menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O MAIOR valor foi \033[0;43m{}\033[m e o MENOR valor foi \033[0;43m{}\033[m.'.format(maior, menor))
print('Acabou!')