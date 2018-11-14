import random

def random_gen():
    rand_num = random.randint(1, 9)
    msg = ""
    for turn in range(5):
        user_guess = int(input('Please guess your magic number (0-10): '))
        if user_guess < rand_num:
            msg = 0
            print('Guess is too low. Try again')
        elif user_guess > rand_num:
            msg =  2
            print('Guess is to high. Try again')
        elif user_guess == rand_num:
            msg = 1
            print('You guessed the number right')
            print('Game is over')
            break
        turn = turn + 1    
    return msg
               
random_gen()