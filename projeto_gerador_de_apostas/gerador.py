from random import randint
armazenamento = list()
usuario = int(input('Quantos números você gostaria de gerar? '))
for n in range(1, usuario + 1):
    gerador = randint(1, 61)
    if gerador in armazenamento:
        gerador = randint(1, 61)
    else:
        armazenamento.append(gerador)
print(armazenamento)
