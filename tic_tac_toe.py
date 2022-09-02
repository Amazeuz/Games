espaços = [i for i in range(1, 10)]
posições_ocupadas = []
movimentos_disponíveis = [1,2,3,4,5,6,7,8,9]
vencedor = False

class JogoDaVelha:
    def __init__(self, letra='X'):
        self.letra = letra

    def tabuleiro(self):
        tabuleiro = f"""
        |  {espaços[0]}  |  {espaços[1]}  |  {espaços[2]}  |
        |  {espaços[3]}  |  {espaços[4]}  |  {espaços[5]}  |
        |  {espaços[6]}  |  {espaços[7]}  |  {espaços[8]}  |
        """
        print(tabuleiro)

    def checa_movimentos_disponíveis(self):
        for i in movimentos_disponíveis:
            if i in posições_ocupadas:
                movimentos_disponíveis.remove(i)

    def turno_letra(self):
        print(f'Vez de {self.letra}, as posições disponíveis são: {movimentos_disponíveis}')
        while True:
            posição_letra = int(input(f'{self.letra} mover para: (1-9) '))
            if posição_letra not in posições_ocupadas:
                espaços[posição_letra - 1] = f'{self.letra}'
                posições_ocupadas.append(posição_letra)
                break
            else:
                print('Posição já preenchida, escolha outra !')

    def checa_vencedor(self):
        global vencedor
        if espaços[0] == self.letra and espaços[3] == self.letra and espaços[6] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
        if espaços[1] == self.letra and espaços[4] == self.letra and espaços[7] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
        if espaços[2] == self.letra and espaços[5] == self.letra and espaços[8] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
        if espaços[0] == self.letra and espaços[1] == self.letra and espaços[2] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
        if espaços[3] == self.letra and espaços[4] == self.letra and espaços[5] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
        if espaços[6] == self.letra and espaços[7] == self.letra and espaços[8] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
        if espaços[0] == self.letra and espaços[4] == self.letra and espaços[8] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
        if espaços[2] == self.letra and espaços[4] == self.letra and espaços[6] == self.letra:
            print(f'{self.letra} é o vencedor!')
            vencedor = True
                ## Refatorar isso porque ta horrível ## 

    def play(self):
        while True:
            print(vencedor)
            self.tabuleiro()

            self.turno_letra()
            self.checa_vencedor()

            if vencedor:
                break

            self.checa_movimentos_disponíveis()

            if len(movimentos_disponíveis) != 0:
                self.letra = 'O'
                self.tabuleiro()

                self.turno_letra()
                self.checa_vencedor()

                self.checa_movimentos_disponíveis()
                
                self.letra = 'X'
            else:
                print('Deu velha!')
                break
            if vencedor:
                break


game1 = JogoDaVelha()
game1.play()