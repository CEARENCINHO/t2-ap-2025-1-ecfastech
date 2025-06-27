# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidataBolsonaro = 0
padreKelmo = 0
simone = 0

eleitores = int(input('São quantos eleitores?: '))

for i in range(eleitores):
    voto = int(input('  Canditatos\n1 - Candidata Bolsonaro\n2 - Padre Kelmo\n3 - Simone\n'))
    if voto == 1:
        candidataBolsonaro += 1
    elif voto == 2:
        padreKelmo += 1
    elif voto == 3:
        simone += 1

print(f'    Resultados\nCandidata Bolsonaro teve {candidataBolsonaro} votos\nPadre Kelmo teve {padreKelmo} votos\nSimone teve {simone} votos')