from random import randint
armazenamento = list()
for n in range(1, 61):
    gerador = randint(1, 61)
    if gerador in armazenamento:
        gerador = randint(1, 61)
    else:
        armazenamento.append(gerador)
