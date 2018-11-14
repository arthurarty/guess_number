import random

def random_gen():
    rand_num = random.randint(0, 10)
    for turn in range(5):
        user_guess = input('Please guess your magic number (0-10): ')
        if user_guess < rand_num:
            print ('Guess is too low. Try again')
        elif user_guess > rand_num:
            print ('Guess is to high. Try again')
        elif user_guess == rand_num:
            print ('You guessed the number right')
            print ('Game Over')
            break
        turn = turn + 1    
                       
random_gen()
