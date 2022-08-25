import random

def carrega_nomes():
    nome = []

    with open('nomes copy.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            nome.append(linha)
    

    randomizador = random.randrange(0,len(nome))
    nome_selecionado = nome[randomizador]
    return nome_selecionado

palavra_escolhida = carrega_nomes()

#palavras = ['Arroz', 'Feijão', 'Batata','Alface', 'Abóbora', 'Tomate', 'Milho', 'Macarrão', 'Azeite','Beringela','Pinhão']
#palavra_escolhida = random.choice(palavras)

erros = 1
letras_usadas = []
resultado = []

for letra in palavra_escolhida:
    resultado.append('_')
    
while erros < 7 and ''.join(resultado) != palavra_escolhida:
    index = 0
    print(resultado)
    #print(palavra_escolhida)

    chute = input('Digite uma letra: ')

    if chute not in palavra_escolhida.lower():
        print(f'Você errou! Você ainda tem {6 - erros} tentativas')
        erros += 1

    if chute in letras_usadas:
        print('Você já usou essa palavra, tente novamente:')
    
    for letra in palavra_escolhida:
        if chute == letra.lower():
            letras_usadas.append(chute)
            resultado[index] = letra
        index += 1

    if chute == palavra_escolhida.lower():
        break


if ''.join(resultado) == palavra_escolhida or chute == palavra_escolhida.lower():
    print(f'Você ganhou ! A palavra secreta era {palavra_escolhida}.')
else:
    print(f'você perdeu KKKKKKKKKJJJJJJJJJJJKKKKKK era {palavra_escolhida}')