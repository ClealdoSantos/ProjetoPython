nota1 = float(input('Digite a PRIMEIRA nota: '))
nota2 = float(input('Digite a SEGUNDA nota: '))
média = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f},o aluno tem média {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno tá de RECUPERAÇÃO')
elif média < 5:
    print('O aluno está REPROVADO')
elif média >= 7:
    print('O aluno está APROVADO')
