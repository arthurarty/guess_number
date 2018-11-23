import random
from utilities import guess_number

def random_gen():
    rand_num = random.randint(1, 9)
    for turn in range(5):
        user_guess = int(input('Please guess your magic number (0-10): '))
        res = guess_number(user_guess, rand_num)
        if res == "Right":
            print(res)
            break
        print(res)
        turn = turn + 1
               
random_gen()