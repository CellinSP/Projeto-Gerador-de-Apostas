from random import randint
from funcoes import enfeite

arquivo = open('historico.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
historico = list()
armazenamento = list()

print('='*60)
print('Bem vindo a loteria! '.center(60))
print('='*60)

print('')
print('Confira a seguir os tipos de loteria:')

enfeite('1','Mega Sena')
enfeite('2','Lotofácil')
enfeite('3','Dupla Sena')
enfeite('4','Quina')
enfeite('5','Super sete')
enfeite('6','Timemania')
enfeite('7','Lotomania')
enfeite('8','Dia de sorte')
enfeite('9','Federal')
enfeite('10','Mega sena da virada')
enfeite('11','Quina de São João')
enfeite('12','Dupla sena de páscoa')
enfeite('13','Lotofácil da independência')
print('-'*60)
enfeite('14','Sair')

escolha = int(input('Digite sua opção: '))
usuario = 0

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
