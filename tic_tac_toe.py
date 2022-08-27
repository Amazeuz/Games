espaços = [i for i in range(1, 10)]
posições_ocupadas = []
movimentos_disponíveis = [1,2,3,4,5,6,7,8,9]
winner = False

def tabuleiro():
    tabuleiro = f"""
|  {espaços[0]}  |  {espaços[1]}  |  {espaços[2]}  |
|  {espaços[3]}  |  {espaços[4]}  |  {espaços[5]}  |
|  {espaços[6]}  |  {espaços[7]}  |  {espaços[8]}  |
 """
    print(tabuleiro)


def turno_x():
    print('Vez de X')
    print(f'As posições disponíveis são: {movimentos_disponíveis}')
    while True:
        posição_x = int(input('X mover para: (1-9) '))
        if posição_x not in posições_ocupadas:
            espaços[posição_x - 1] = 'X'
            posições_ocupadas.append(posição_x)
            break
        else:
            print('Posição já preenchida, escolha outra !')


def turno_o():
    print('Vez de O')
    print(f'As posições disponíveis são: {movimentos_disponíveis}')
    while True:
        posição_o = int(input('O mover para: (1-9) '))
        if posição_o not in posições_ocupadas:
            espaços[posição_o - 1] = 'O'
            posições_ocupadas.append(posição_o)
            break
        else:
            print('Posição já preenchida, escolha outra !')


def checa_movimentos_disponíveis():
    for i in movimentos_disponíveis:
        if i in posições_ocupadas:
            movimentos_disponíveis.remove(i)


def checa_o():
    global winner
    if espaços[0] == 'O' and espaços[3] == 'O' and espaços[6] == 'O':
        print('O é o vencedor!')
        winner = True
    if espaços[1] == 'O' and espaços[4] == 'O' and espaços[7] == 'O':
        print('O é o vencedor!')
        winner = True
    if espaços[2] == 'O' and espaços[5] == 'O' and espaços[8] == 'O':
        print('O é o vencedor!')
        winner = True
    if espaços[0] == 'O' and espaços[1] == 'O' and espaços[2] == 'O':
        print('O é o vencedor!')
        winner = True
    if espaços[3] == 'O' and espaços[4] == 'O' and espaços[5] == 'O':
        print('O é o vencedor!')
        winner = True
    if espaços[6] == 'O' and espaços[7] == 'O' and espaços[8] == 'O':
        print('O é o vencedor!')
        winner = True
    if espaços[0] == 'O' and espaços[4] == 'O' and espaços[8] == 'O':
        print('O é o vencedor!')
        winner = True
    if espaços[2] == 'O' and espaços[4] == 'O' and espaços[6] == 'O':
        print('O é o vencedor!')
        winner = True


def checa_x():
    global winner
    if espaços[0] == 'X' and espaços[3] == 'X' and espaços[6] == 'X':
        print('X é o vencedor!')
        winner = True
    if espaços[1] == 'X' and espaços[4] == 'X' and espaços[7] == 'X':
        print('X é o vencedor!')
        winner = True
    if espaços[2] == 'X' and espaços[5] == 'X' and espaços[8] == 'X':
        print('X é o vencedor!')
        winner = True
    if espaços[0] == 'X' and espaços[1] == 'X' and espaços[2] == 'X':
        print('X é o vencedor!')
        winner = True
    if espaços[3] == 'X' and espaços[4] == 'X' and espaços[5] == 'X':
        print('X é o vencedor!')
        winner = True
    if espaços[6] == 'X' and espaços[7] == 'X' and espaços[8] == 'X':
        print('X é o vencedor!')
        winner = True
    if espaços[0] == 'X' and espaços[4] == 'X' and espaços[8] == 'X':
        print('X é o vencedor!')
        winner = True
    if espaços[2] == 'X' and espaços[4] == 'X' and espaços[6] == 'X':
        print('X é o vencedor!')
        winner = True


while True:
    tabuleiro()

    turno_x()
    checa_x()

    if winner == True:
        break

    checa_movimentos_disponíveis()

    if len(movimentos_disponíveis) != 0:
        tabuleiro()

        turno_o()
        checa_o()

        checa_movimentos_disponíveis()
    else:
        print('Deu velha!')
        break