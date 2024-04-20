from time import sleep
from funções_montante_e_juros_simples import calcular_montante, calcular_juros_simples


def sep(caracter, tamanho):
    print(f'{caracter}' * tamanho)


# Entrada das informações do investimento
capital = float(input('Investimento inicial: R$ '))

sep('-', 20)

taxa = float(input('Taxa de juros: '))
exib_taxa = taxa

sep('-', 20)

porcentagem = input(f'''Você digitou a taxa de juros em porcentagem ({taxa}%)? [S/N] ''')
if porcentagem in 'SsSimsim':
    porcentagem = True
else:
    porcentagem = False
    exib_taxa = taxa * 100

sep('-', 20)

tempo = float(input('Tempo de investimento: '))


# Processamento dos dados para cálculo
J = calcular_juros_simples(capital, taxa, tempo, porcentagem=porcentagem)
M = calcular_montante(capital, J)


# Exibição dos resultados
print()
sep('¨', 35)
print(' ' * 6, 'Relatório da Poupança')
sep('¨', 35)
sleep(2)
print(f'''Você investiu R${capital:.2f} com taxa de {exib_taxa}% por um período de {tempo}''')
sleep(3)
print()
print(f'Juros acumulados: R${J:.2f}')
sleep(2)
print(f'Seu montante final foi de R${M:.2f}')
sleep(2)
print()
