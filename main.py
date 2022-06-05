import random


def guess_number(correct_number):
    correct = False
    while not correct:
        guessed = int(input(f'Guess a number:'))
        print(guessed)
        if correct_number == guessed:
            correct = True
        print(f'You guessed: {guessed}')
    print(f'... and it\'s correct!')


guess_number(10)
