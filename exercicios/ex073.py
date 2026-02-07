print("=" * 50)
print("                  TABELA BRASILEIRAO")
times = ('bragantino', 'Palmeiras', 'Chapecoense', 'Mirassol'
        ,'Fluminense', 'Bahia', 'Sao Paulo', 'Botafogo', 'Gremio'
        , 'Athletico-PR', 'Coritiba', 'EC Vitoria', 'Flamengo'
        , 'Atletico-MG', 'Vasco da Gama', 'Internacional'
        , 'Santos', 'Remo', 'corinthians', 'Cruzeiro')
print("=" * 50)
for time in times:
        print(time)
print('=' * 50)
print(f'Os 5 Primeiros sao {times[0:5]}')
print('=-' * 50)
print(f'Os 4 Ultimos times sao {times[-4:]}')
print('=-' * 50)
print("==========OS TIMES EM ORDEM ALFABETICA==========")
print('\n'.join(sorted(times)))
print(f'O Chapecoense esta na {times.index("Chapecoense")+1} posicao')