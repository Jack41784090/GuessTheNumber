import random


def guess_number(max_number):
    correct = False
    random_number = random.randint(1, max_number)
    while not correct:
        guessed = int(input(f'Guess a number between 1 and {max_number}:'))
        if random_number > guessed:
            print(f'Go higher!')
        elif random_number < guessed:
            print(f'Go lower!')
        elif random_number == guessed:
            correct = True
        print(f'You guessed {guessed} and it is { "correct" if correct else "incorrect" }')


max_num = int(input(f'What is the upper limit of the guess?:'))
guess_number(max_num)
