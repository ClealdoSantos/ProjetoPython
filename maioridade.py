from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
     nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
     idade = atual - nasc
     if idade >= 18:
         totmaior += 1
     else:
         totmenor += 1
print('Ao todo tivemos \033[31m{}\033[m pessoas maiores de idade'.format(totmaior))
print('E também tivemos \033[31m{}\033[m pessoas menores de idade'.format(totmenor))
