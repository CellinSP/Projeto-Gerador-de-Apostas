from random import randint
from time import sleep
from termcolor import colored

arquivo = open('historico.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()

historico = list()
armazenamento = list()
aposta = list()
numeros = list()

print('='*60)
print('Bem vindo a loteria! '.center(60))
print('='*60)

print('')
print('Dobre o seu dinheiro se acertar os números que serão gerados pela maquina!')
while True:
    print('1-Aposta\n2-Histórico\n3-Sair')
    escolha = int(input('Digite o número de uma opção para continuar: '))
    if escolha == 1:
        break
    elif escolha == 2:
        print('-'*17)
        print(conteudo, end='')
        print('-'*17)
    elif escolha == 3:
        print('Programa encerrado.')
        exit()
aposta.append(float(input('Digite o valor da sua aposta: R$')))
for n in range(1, 7):
    numeros.append(int(input(f'Digite o {n}° número, de 01 a 60 (sem repetir): ')))

for n in range(1, 7):
    gerador = randint(1, 60)
    while gerador in armazenamento:
        gerador = randint(1, 60)
    armazenamento.append(gerador)
    arquivo = open('historico.txt', 'a', encoding='utf-8')
    arquivo.write((str(gerador) + ' '))
arquivo.write('\n')
arquivo.close()
print('Os números gerados foram: ', end='')
acertos = 0
for n in range(0, 6):
    sleep(1)
    if armazenamento[n] in numeros:
        acertos += 1
        print(colored(f'{armazenamento[n]:02d}', 'green'), end=' ')
    else:
        print(colored(f'{armazenamento[n]:02d}', 'red'), end=' ')
if acertos == 6:
    print('\nPARABÉNS! Você acertou todos os números.')
else:
    print(f'\nVocê acertou {acertos} número(s). Mais sorte na próxima vez.')
while True:
    print('1-Histórico\n2-Limpar histórico\n3-Sair')
    escolha = int(input('Digite o número de uma opção para continuar: '))
    if escolha == 1:
        print('-'*17)
        print(conteudo, end='')
        print('-'*17)
    elif escolha == 2:
        with open('historico.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('')
            arquivo.close()
    elif escolha == 3:
        print('Programa encerrado.')
        exit()
