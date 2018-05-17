import random

print('----------------------------------------------')
print('     GUESS THAT NUMBER GAME')
print('----------------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {1}, your guess of {0} was too low. Try Again :) '.format(guess, name))
    elif guess > the_number:
        print('Sorry {1}, your guess of {0} was too high. Try Again :) '.format(guess, name))
    else:
        print('Congratulations {1}, your guess of {0} was correct!'.format(guess, name))






