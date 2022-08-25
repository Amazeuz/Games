espaços = [i for i in range(1, 10)]
posições_ocupadas = []
movimentos_disponíveis = [1,2,3,4,5,6,7,8,9]
ops = False

while True:

    tabuleiro = f"""
|  {espaços[0]}  |  {espaços[1]}  |  {espaços[2]}  |
|  {espaços[3]}  |  {espaços[4]}  |  {espaços[5]}  |
|  {espaços[6]}  |  {espaços[7]}  |  {espaços[8]}  |
 """

    print('--------------------------------------')
    print(tabuleiro)
    print('Vez de X')
    print(f'As posições disponíveis são: {movimentos_disponíveis}')
    posição_x = int(input('X mover para: (1-9) '))
    
    if posição_x not in posições_ocupadas:
        espaços[posição_x - 1] = 'X'
        posições_ocupadas.append(posição_x)
    else:
        print('Posição já preenchida, escolha outra !')
        continue

    tabuleiro = f"""
|  {espaços[0]}  |  {espaços[1]}  |  {espaços[2]}  |
|  {espaços[3]}  |  {espaços[4]}  |  {espaços[5]}  |
|  {espaços[6]}  |  {espaços[7]}  |  {espaços[8]}  |
 """

    print(tabuleiro)

    if espaços[0] == 'X' and espaços[3] == 'X' and espaços[6] == 'X':
        print('X é o vencedor!')
        break
    if espaços[1] == 'X' and espaços[4] == 'X' and espaços[7] == 'X':
        print('X é o vencedor!')
        break
    if espaços[2] == 'X' and espaços[5] == 'X' and espaços[8] == 'X':
        print('X é o vencedor!')
        break
    if espaços[0] == 'X' and espaços[1] == 'X' and espaços[2] == 'X':
        print('X é o vencedor!')
        break
    if espaços[3] == 'X' and espaços[4] == 'X' and espaços[5] == 'X':
        print('X é o vencedor!')
        break
    if espaços[6] == 'X' and espaços[7] == 'X' and espaços[8] == 'X':
        print('X é o vencedor!')
        break
    if espaços[0] == 'X' and espaços[4] == 'X' and espaços[8] == 'X':
        print('X é o vencedor!')
        break
    if espaços[2] == 'X' and espaços[4] == 'X' and espaços[6] == 'X':
        print('X é o vencedor!')
        break

    for i in movimentos_disponíveis:
        if i in posições_ocupadas:
            movimentos_disponíveis.remove(i)
    
    print('--------------------------------------')
    print(tabuleiro)
    print('Vez de O')
    print(f'As posições disponíveis são: {movimentos_disponíveis}')
    posição_o = int(input('O mover para: (1-9) '))
    
    if posição_o not in posições_ocupadas:
        espaços[posição_o - 1] = 'O'
        posições_ocupadas.append(posição_o)
    else:
        print('Posição já preenchida, escolha outra !')
        continue
    

    if espaços[0] == 'O' and espaços[3] == 'O' and espaços[6] == 'O':
        print('O é o vencedor!')
        break
    if espaços[1] == 'O' and espaços[4] == 'O' and espaços[7] == 'O':
        print('O é o vencedor!')
        break
    if espaços[2] == 'O' and espaços[5] == 'O' and espaços[8] == 'O':
        print('O é o vencedor!')
        break
    if espaços[0] == 'O' and espaços[1] == 'O' and espaços[2] == 'O':
        print('O é o vencedor!')
        break
    if espaços[3] == 'O' and espaços[4] == 'O' and espaços[5] == 'O':
        print('O é o vencedor!')
        break
    if espaços[6] == 'O' and espaços[7] == 'O' and espaços[8] == 'O':
        print('O é o vencedor!')
        break
    if espaços[0] == 'O' and espaços[4] == 'O' and espaços[8] == 'O':
        print('O é o vencedor!')
        break
    if espaços[2] == 'O' and espaços[4] == 'O' and espaços[6] == 'O':
        print('O é o vencedor!')
        break

    for i in movimentos_disponíveis:
        if i in posições_ocupadas:
            movimentos_disponíveis.remove(i)

    if len(movimentos_disponíveis) == 0:
        print('Deu velha !')
        break