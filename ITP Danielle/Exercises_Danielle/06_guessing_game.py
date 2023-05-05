import random
magic_number = random.randint(1,10)

num_Guess = 1
win = False

while num_Guess <= 3:
    print ("Guess the magic number between 1 and 10: ")
    user_guess = int(input())
    if user_guess == magic_number:
        print("You got it!")
        win = True
        break
    elif user_guess + 1 == magic_number or user_guess - 1 == magic_number:
        print("So close!")
    else:
        print("Way off!")
    num_Guess = num_Guess + 1
    # end while 
if win:
    print("You win!")
else:
    print("You lose!")
    



