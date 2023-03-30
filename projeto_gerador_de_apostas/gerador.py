from random import randint
from time import sleep
from funcoes import enfeite

arquivo = open('historico.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
historico = list()
armazenamento = list()
aposta = list()
numeros = list()

print('='*60)
print('Bem vindo a loteria! '.center(60))
print('='*60)

print('')
print('Dobre o seu dinheiro se acertar os números que serão gerados pela maquina!')

aposta.append(float(input('Digite o valor da sua aposta: R$')))
for n in range(1, 7):
    numeros.append(int(input(f'Digite o {n}° número, de 01 a 60 (sem repetir): ')))

for n in range(1, 7):
    gerador = randint(1, 60 + 1)
    while gerador in armazenamento:
        gerador = randint(1, 60 + 1)
    armazenamento.append(gerador)
    arquivo = open('historico.txt', 'a', encoding='utf-8')
    arquivo.write((str(gerador) + ' '))
arquivo.write('\n')
arquivo.close()
print(f'Os números gerados foram: {armazenamento} ')
if numeros in armazenamento:
    print('PARABÉNS! Você acertou.')
else:
    print('Você errou! Mais sorte na próxima vez.')
