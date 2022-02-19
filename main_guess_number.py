from random import *


def start_game():
	print("Welcome to  the Number Guessing Game!\nI'm thinking of a number between 1 an 100.")
	random_number = randint(1, 100)
	end = False

	if input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
		attempts = 5
	else:
		attempts = 10

	while attempts > 0 and end == False:
		print(f"You have {attempts} attempts to guess the number.")
		guess = int(input("Make a guess: "))

		if guess > random_number:
			print("To high.")
			attempts -= 1
		elif guess < random_number:
			print("Too low.")
			attempts -= 1
		elif guess == random_number:
			print("Yes. You Win!")
			end = True
		else:
			print("Not a number!")

		if attempts > 0 and end == False:
			print("Guess again.")
		elif attempts == 0:
			print("Game Over!")

	if input("Repeat? 'y' or 'n': ") == 'y':
		start_game()


start_game()
