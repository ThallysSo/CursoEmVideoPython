times = (
    'São Paulo',
    'Atlético-MG',
    'Flamengo',
    'Grêmio',
    'Internacional',
    'Palmeiras',
    'Fluminense',
    'Santos',
    'Corinthians',
    'Athletico-PR',
    'Ceará',
    'Bragantino',
    'Atlético-GO',
    'Sport',
    'Fortaleza',
    'Bahia',
    'Vasco',
    'Goiás',
    'Botafogo',
    'Coritiba')

# times[0:5]
print('=' * 25)
print('Os primeiros 5 colocados')
print('=' * 25)
for c in range(0, 5):
    print(c+1, '-', times[c])

# times[-4:]
print('=' * 25)
print('Os 4 últimos colocados')
print('=' * 25)
for c in range(-4, 0):
    print(len(times) + c+1, '-', times[c])

# sorted(times)
print('=' * 25)
print('Times em ordem alfabética')
print('=' * 25)
times_ordem = sorted(times)
for c in range(0, len(times)):
    print(c+1, '-', times_ordem[c])

# times.index('Fluminense')
print('=' * 25)
print('Posição do Fluminense')
print('=' * 25)
for c in range(0, len(times)):
    if times[c] == 'Fluminense':
        print(f'O {times[c] } está na {c+1}º posição')