import random

print('Bem vindo ao jogo de pedra papel tesoura !')

pedra_papel_tesoura = ['pedra', 'papel', 'tesoura']

pontuação_usuário = 0
pontuação_oponente = 0


while pontuação_usuário < 5 or pontuação_oponente < 5: #pontuação > -3 and pontuação < 5:

    item = input('Selecione o seu item: ')

    ia_item = random.choice(pedra_papel_tesoura)
    
    print(f'O oponente selecionou {ia_item.upper()}')

    if not item.lower() in pedra_papel_tesoura:
        print('Selecione um item válido !!!!!')
        continue

    if item.lower() == 'pedra':
        if ia_item == 'tesoura':
            print('Você ganhou !')
            pontuação_usuário += 1
            print(f'Sua pontuação é de {pontuação_usuário}')
        elif ia_item == 'pedra':
            print('Empate! Tente novamente:')
            continue
        else:
            print('Você perdeu.')
            pontuação_oponente += 1
            print(f'A pontuação do oponente é de {pontuação_oponente}')


    if item.lower() == 'papel':
        if ia_item == 'pedra':
            print('Você ganhou !')
            pontuação_usuário += 1
            print(f'Sua pontuação é de {pontuação_usuário}')
        elif ia_item == 'papel':
            print('Empate! Tente novamente')
            continue
        else:
            print('Você perdeu.')
            pontuação_oponente += 1
            print(f'A pontuação do oponente é de {pontuação_oponente}')


    if item.lower() == 'tesoura':
        if ia_item == 'papel':
            print('Você ganhou !')
            pontuação_usuário += 1
            print(f'Sua pontuação é de {pontuação_usuário}.')
        elif ia_item == 'tesoura':
            print('Empate! Tente novamente')
            continue
        else:
            print('Você perdeu.')
            pontuação_oponente += 1
            print(f'A pontuação do oponente é de {pontuação_oponente}')
        
    if pontuação_usuário == 5:
        print('Você ganhou o jogo!')
        break
    elif pontuação_oponente == 5:
        print('Você perdeu o jogo.')
        break


print('Fim de jogo.')

