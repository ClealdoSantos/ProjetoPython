from time import sleep
n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] \033[35mSOMAR\033[m
    [ 2 ] \033[31mMULTIPLICA\033[m
    [ 3 ] \033[36mMAIOR\033[m
    [ 4 ] \033[32mNOVOS NÚMEROS\033[m
    [ 5 ] \033[33mSAIR\033[m''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado entre {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o MAIOR valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Digite os números novamente: ')
        n1 = int(input('Digite o PRIMEIRO valor: '))
        n2 = int(input('Digite o SEGUNDO valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    print('=\033[31m*\033[m='*10)
    sleep(2)
print('Fim do Programa! Volte sempre!')
