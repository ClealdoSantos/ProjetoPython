soma = cont = 0
while True:
    num = int(input('Digite um número ( 13 para parar): '))
    if num == 13:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}.')
