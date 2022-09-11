from time import sleep
import curses

for i in range(18000000000000000):   #repetindo o progama
    sleep(2)
    print('\n')

#codigo aqui
    n1 = 'insíra a operação desejada: '
    n1 += '\n+ para adição'
    n1 += '\n- para subtração'
    n1 += '\n* para multiplicação'
    n1 += '\n/ para divisão \nOperação: '

    operacao = input(n1)

    num_1 = int(input('Entre com o primeiro número: '))
    num_2 = int(input('Entre com o segundo número: '))

    if operacao == '+':
        print(f'Operação: {num_1} {operacao} {num_2} = {num_1 + num_2}')

    elif operacao == '-':
        print(f'Operação: {num_1} {operacao} {num_2 } = {num_1 - num_2}')

    elif operacao == '*':
        print(f'Operação: {num_1} {operacao} {num_2} = {num_1 * num_2}')

    elif operacao == '/':
        print(f'Operação: {num_1} {operacao} {num_2} = {num_1 / num_2}')

    else:
        print('Operação matemática inválida para essa calculadora, tente novamente!')

sleep(2)