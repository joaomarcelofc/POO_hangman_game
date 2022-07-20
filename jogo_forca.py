# Hangman Game (Jogo da forca)
# Python - Programação Orientada a Objetos
#Lab03 - DataScienceAcademy
# João Marcelo Fonseca Cunha

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Hangman:
	
	# método construtor __init__, incluindo listas vazias de letras certas e letras erradas
	def __init__(self, palavra):
		self.palavra = palavra
		self.letras_certas = []
		self.letras_erradas = []


	# método para verificar se a letra está na palavra, e incluir esta mesma letra na lista correta
	def guess(self, letra):
		if letra in self.palavra and letra not in self.letras_certas:
			self.letras_certas.append(letra)
		elif letra not in self.palavra and letra not in self.letras_erradas:
			self.letras_erradas.append(letra)
		else:
			return False
		return True

	# método para verificar se o jogo chegou ao final. O jogo acaba quando vence(método hangman_ganhou), ou quando o len de letras erradas for igual a 6
	# onde será acessado o último elemento da lista board, que é o desenho final da forca
	def hangman_fim(self):
		return self.hangman_ganhou() or (len(self.letras_erradas) == 6)

	# método para verificar se o jogador ganhou. Ele ganha se não houver nenhum caracter '_' na palavra oculta	
	def hangman_ganhou(self):
		if '_' not in self.esconder_palavra():
			return True
		return False


	# método para não mostrar as letras na palavra
	def esconder_palavra(self):
		xyz = ''
		for letra in self.palavra:
			if letra not in self.letras_certas:
				xyz += '_'
			else:
				xyz += letra
		return xyz
		

	# método que vai mostrar board de acordo com o len da listra de letras certas, mostrar palavra oculta, mostrar letras certas, mostrar letras erradas
	def print_game_status(self):
		print(board[len(self.letras_erradas)])
		print('\nPalavra', self.esconder_palavra())
		print('\nLetras certas: ',)
		for x in self.letras_certas:
			print(x, end=' - ')
		print('\nLetras erradas: ',)
		for y in self.letras_erradas:
			print(y, end=' - ')
 
# função para escolher uma palavra aleatória no arquivo palavras.txt
def palavra_aleatoria():
		with open('palavras.txt', 'rt') as arquivo:
			banco = arquivo.readlines()
		return banco[random.randint(0, len(banco))].strip()


def main():

	# objeto
	game = Hangman(palavra_aleatoria())

	# enquanto o jogo não tiver terminado: PRINT STATUS, SOLICITA LETRA, FAZ LEITURA DO CARACTER
	while not game.hangman_fim():
		game.print_game_status()
		usuario_input = input('\nDigite uma letra: ')
		game.guess(usuario_input)

	print(game.print_game_status())

	if game.hangman_ganhou():
		print('Parabéns!! Você ganhou!')
	else:
		print('GAME OVER! Você perdeu!')
		print('A palavra certa era', game.palavra)

if __name__ == "__main__":
	main() 



