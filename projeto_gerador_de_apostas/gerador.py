#bibliotecas importadas
from random import randint
from time import sleep
from termcolor import colored

#loop para fazer o tratamento de erros
while True:
    sleep(2)
    try:
        #varoáveis referentes ao histórico do programa
        arquivo = open('historico.txt', 'r', encoding='utf-8')
        conteudo = arquivo.read()
        #listas para guardar os números gerados, valor da
        # aposta e palpites do usuário, respectivamente
        armazenamento = list()
        aposta = list()
        numeros = list()
        #interface
        print('='*60)
        print('Bem vindo a loteria! '.center(60))
        print('='*60)
        print('')
        print('Dobre o seu dinheiro se acertar os números que serão gerados pela maquina!')
        #menu de opções
        while True:
            print('1-Aposta\n2-Histórico\n3-Sair')
            escolha = int(input('Digite o número de uma opção para continuar: '))
            #validação da opção digitada
            if escolha < 1 or escolha > 3:
                raise ValueError
            if escolha == 1:
                break
            elif escolha == 2:
                print('-'*17)
                print(conteudo, end='')
                print('-'*17)
            elif escolha == 3:
                confirmacao = input(colored('Tem certeza de que '
                                    'gostaria de sair do programa? ', 'yellow')).lower().strip()[0]
                #validação da opção digitada
                if confirmacao != 's' and confirmacao != 'n':
                    raise TypeError
                elif confirmacao == 's':
                    print('Encerrando o programa...')
                    break
        if escolha == 3:
            break
        valor = float(input('Digite o valor da sua aposta: R$').replace(',', '.').strip())
        #validação do valor digitado
        if valor <= 0:
            raise ValueError
        aposta.append(valor)
        CONT = 1
        #validação para o número não ser repetido ou fora do intervalo númerico permitido
        while len(numeros) != 6:
            verificacao = int(input(f'Digite o {CONT}° número, de 01 a 60 (sem repetir): '))
            if verificacao not in numeros:
                if verificacao > 0 and verificacao < 61:
                    numeros.append(verificacao)
                    CONT += 1
                else:
                    raise ValueError
            else:
                print(colored('ERRO! Por favor, não repita o mesmo número.', 'red'))
        #validação para não gerar números repetidos ao mesmo tempo que adiciona ao histórico
        for n in range(1, 7):
            gerador = randint(1, 60)
            while gerador in armazenamento:
                gerador = randint(1, 60)
            armazenamento.append(gerador)
            arquivo = open('historico.txt', 'a', encoding='utf-8')
            arquivo.write(f"{gerador:02d} ")
        arquivo.write('\n')
        arquivo.close()
        print('Os números gerados foram: ', end='')
        ACERTOS = 0
        #revelação do resultado da aposta do usuário
        for n in range(0, 6):
            sleep(1)
            if armazenamento[n] in numeros:
                ACERTOS += 1
                print(colored(f'{armazenamento[n]:02d}', 'green'), end=' ')
            else:
                print(colored(f'{armazenamento[n]:02d}', 'red'), end=' ')
        if ACERTOS == 6:
            print('\nPARABÉNS! Você acertou todos os números.')
            print(f'Você ganhou R${aposta[0]*2}')
        else:
            print(f'\nVocê acertou {ACERTOS} número(s). Mais sorte na próxima vez.')
        #menu de opções
        while True:
            print('1-Histórico\n2-Limpar histórico\n3-Sair')
            escolha = int(input('Digite o número de uma opção para continuar: '))
            #validação da opção digitada
            if escolha < 1 or escolha > 3:
                raise ValueError
            if escolha == 1:
                print('-'*17)
                print(conteudo, end='')
                print('-'*17)
            elif escolha == 2:
                confirmacao = input(colored('Tem certeza de que '
                                    'gostaria de limpar o histórico? ','yellow')).lower().strip()[0]
                #validação da opção digitada
                if confirmacao != 's' and confirmacao != 'n':
                    raise TypeError
                elif confirmacao == 's':
                    print('Limpando o histórico...')
                    with open('historico.txt', 'w', encoding='utf-8') as arquivo:
                        arquivo.write('')
                        arquivo.close()
            elif escolha == 3:
                confirmacao = input(colored('Tem certeza de que '
                                    'gostaria de sair do programa? ', 'yellow')).lower().strip()[0]
                #validação da opção digitada
                if confirmacao != 's' and confirmacao != 'n':
                    raise TypeError
                elif confirmacao == 's':
                    print('Encerrando o programa...')
                    break
        if escolha == 3:
            break
    #tratamento de erros
    except FileNotFoundError:
        print(colored('ERRO! Arquivo "historico.txt" não encontrado. '
                      'Certifique-se de que o arquivo existe '
                      'e está na pasta correta.', 'red'))
    except PermissionError:
        print(colored('ERRO! O programa não tem permissão para acessar ou escrever no arquivo '
                      '"historico.txt". Certifique-se de que o arquivo não está sendo usado '
                      'por outro programa e que você tem permissão para acessa-lo. ', 'red'))
    except ValueError:
        print(colored('ERRO! Por favor digite um número válido', 'red'))
    except TypeError:
        print(colored('ERRO! Por favor digite "sim" ou "não"', 'red'))
