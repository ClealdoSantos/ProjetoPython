times = ('Athletico-PR', 'Bahia', 'Botafogo', 'Atlético-MG',
         'Bragantino', 'Palmeiras', 'Flamengo', 'São Paulo',
         'Internacional', 'Cruzeiro', 'Grêmio', 'Fortaleza',
         'Criciúma', 'Corinthians', 'Juventude', 'Fluminense',
         'Vasco da Gama', 'EC Vitória', 'Atlético-GO', 'Cuiabá')
print('\033[33m *\033[m' * 15)
print('{:^40}'.format(' \033[34;43mBRASILEIRÃO 2024\033[m '))
print('\033[32m *\033[m' * 15)
print(f'A lista dos times: {times}')
print('-*' * 15)
print(f'Os cinco primeiros times: {times[0:5]}')
print(f'-*' * 15)
print(f'A lista dos times em ordem alfabética: {sorted(times)}')
print('-*' * 15)
print(f'Os 4 últimos na zona são: {times[-4:]}')
print('-*' * 15)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')
print('-*' * 15)
