print(' ---* Gerador de PA *---')
print('-\033[31m*\033[m'*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Qual a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão Aritmética finalizada com \033[4;36m{}\033[m termos mostrados.'.format(total))