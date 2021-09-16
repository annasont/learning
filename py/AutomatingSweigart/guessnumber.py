"""Game: guess a number"""

import random

print('I am thinking of a number between 1 and 20. \nTake a guess!')
randomNumber = random.randint(1, 21)
numberOfGuesses = 0

while True:
    guess = int(input())
    if guess == randomNumber:
        numberOfGuesses += 1
        print('Congratulation! The number I was thinking about is %s! Number of guesses: %s' % (randomNumber, numberOfGuesses))
        break
    elif guess < 1:
        print('Numer can not be lower than 1!')
    elif guess > 20:
        print('Numer can not be higher than 20!')
    elif guess > randomNumber:
        print('Your guess is too high')
        numberOfGuesses += 1
        continue
    elif guess < randomNumber:
        numberOfGuesses += 1
        print('Your guess is too low')
        continue

