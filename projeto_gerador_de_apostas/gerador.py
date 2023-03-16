from random import randint

arquivo = open('historico.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
historico = list()
armazenamento = list()

usuario = int(input('Quantos números você gostaria de gerar? '))

for n in range(1, usuario + 1):
    gerador = randint(1, 61)
    while gerador in armazenamento:
        gerador = randint(1, 61)
    armazenamento.append(gerador)
    arquivo = open('historico.txt', 'a', encoding='utf-8')
    arquivo.write((str(gerador) + ' '))
arquivo.write('\n')
arquivo.close()
print(armazenamento)
