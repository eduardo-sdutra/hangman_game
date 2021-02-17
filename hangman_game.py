from hangman_words import words_list
from hangman_score import score
from time import sleep
from random import *
from os import system

def get_word(list_input):
	return choice(list_input).upper()

def game_display(word_, tries):
	system('cls')
	if tries == 6:
		print(score[0])
	elif tries == 5:
		print(score[1])
	elif tries == 4:
		print(score[2])
	elif tries == 3:
		print(score[3])
	elif tries == 2:
		print(score[4])
	elif tries == 1:
		print(score[5])
	else:
		print(score[6])
	print(word_)

def attempt_func():
	return input('Type your guess: ').upper()

def char_check(char, word, word_):
	newWord_list = list(word_)
	for i in range(0, len(word)):
		if char == word[i]:
			newWord_list[i] = char
	newWord_ = ''.join(newWord_list)
	return newWord_

def replay():
	return input("To replay, type 'Y'. To quit, type anything: ").upper().startswith('Y')

while True:
	list_words = [' '] * 5
	guessed_char = []
	guessed_word = []
	guess_attempt = ''
	theTries = 6
	theWord = get_word(words_list)
	theWord_ = '_' * len(theWord)
	game_on = True
	game_display(theWord_, theTries)
	print('Welcome to the hangman game!')
	print('The game begins in 3 seconds.')
	sleep(3)

	while game_on:
		game_display(theWord_, theTries)
		# Verifies if the plater won.
		if theWord_ == theWord:
			print('You won!')
			game_on = False
			break
		# Verifies if the player lost.
		if theTries == 0:
			print('Sorry, you lost.')
			game_on = False
			break
		# Allows the player to make an attempt.
		guess_attempt = attempt_func()
		# Verifies if the attempt have already been guessed.
		if guess_attempt in guessed_word:
			print('You already tried this word.')
			guess_attempt = attempt_func()
		elif guess_attempt in guessed_char:
			print('You already tried this character.')
			guess_attempt = attempt_func()
		# Verifies if 'attempt' is a word or a char.
		if len(guess_attempt) > 1:
			guessed_word.append(guess_attempt)
			if guess_attempt == theWord:
				print('You won!')
				game_on = False
			else:
				theTries -= 1
				print('Wrong word!')
				sleep(0.5)
		elif len(guess_attempt) == 1:
			guessed_char.append(guess_attempt)
			if guess_attempt in theWord:
				if guess_attempt == theWord:
					print('You won!')
					game_on = False
				else:
					theWord_ = char_check(guess_attempt, theWord, theWord_)
			else:
				theTries -= 1
				print('Wrong letter!')
				sleep(0.5)
		else:
			print('Invalid input.')
	
	if not replay():
		break
