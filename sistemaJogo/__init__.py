from random import randint

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''',
         '''
+---+
|   |
O   |
    |
    |
    |
=========''',
         '''
+---+
|   |
O   |
|   |
    |
    |
=========''',
         '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''',
         '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''',
         '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''',
         '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Forca:
    # Metódo construtor
    def __init__(self, word):
        self.word = word
        self.guessed_letter = []
        self.missed_letter = []

    # Metódo para advinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letter:
            self.guessed_letter.append(letter)
        elif letter not in self.word and letter not in self.missed_letter:
            self.missed_letter.append(letter)
        else:
            return False
        return True

    # Metódo para verificar se o jogo terminou
    def player_over(self):
        return self.player_won() or (len(self.missed_letter) == 6)

    # Metódo para verificar se o jogador ganhou
    def player_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Metódo para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letter:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Metódo para chegar o status do jogo e imprimir o boneco
    def game_status(self):
        print(board[len(self.missed_letter)])
        print('\nPalavra ', self.hide_word())
        print('\nLetras Erradas: ')
        for letter in self.missed_letter:
            print(letter)
        print()
        print('Letras Corretas: ')
        for letter in self.guessed_letter:
            print(letter)
        print()


# Função para ler uma palavra de forma aleatória do banco de palavras
def word_random():
    with open("Palavras.txt", "r") as palavra:
        rdw = palavra.readlines()
        return rdw[randint(0, len(rdw) - 1)].strip()


def main():
    # Objeto
    game = Forca(word_random())

    while not game.player_over():
        game.game_status()
        game.guess(str(input("Qual a próxima letra? ")))

    game.game_status()

    if game.player_won():
        print("Parabéns, você ganhou!")
    else:
        # print("Que pena, você perdeu!")
        print(f"\nA palavra era {game.word}")


