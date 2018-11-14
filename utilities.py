def guess_number(user_guess, rand_num):
    if user_guess < rand_num:
        msg = "Low"
    elif user_guess > rand_num:
        msg =  "High"
    elif user_guess == rand_num:
        msg = "Right"
    return msg
            