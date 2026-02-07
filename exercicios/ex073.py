times = ('bragantino', 'Palmeiras', 'Chapecoense', 'Mirassol'
        ,'Fluminense', 'Bahia', 'Sao Paulo', 'Botafogo', 'Gremio'
        , 'Athletico-PR', 'Coritiba', 'EC Vitoria', 'Flamengo'
        , 'Atletico-MG', 'Vasco da Gama', 'Internacional'
        , 'Santos', 'Remo', 'corinthians', 'Cruzeiro')

for time in times:
        print('=' * 50)
        print(time)
print('=' * 50)
print(f'Os 5 Primeiros sao {times[0:5]}')
print('=-' * 50)
print(f'Os 4 Ultimos times sao {times[-4:]}')
print('=-' * 50)
print(f'\nTimes em ordem alfabetica {sorted(times)}', end=' ')
print(f'O Chapecoense esta na {times.index("Chapecoense")} posicao')