print('\033[7;30;44m-=\033[m'*20)
print('ANALISANDOR DE TRIÂNGULOS')
print('\033[0;30;44m-=\033[m'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;30;44m Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('\033[0;30;44m Os segmentos acima NÃO FORMAM triângulo!')
