from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem \033[4;36m{}\033[m anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[0;31mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[0;31mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[0;31mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[0;31mSÊNIOR\033[m')
else:
    print('Classificaçaõ: \033[0;31mMASTER\033[m')