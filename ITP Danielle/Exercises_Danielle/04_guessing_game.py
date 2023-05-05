import random
magic_number = random.randint(1,10)
print(magic_number) # print this to test and ensure code is working correctly)
user_guess = int(input("Guess the magic number between 1-10:"))
if user_guess == magic_number:
    print("You got it!")
elif user_guess + 1 == magic_number or user_guess - 1 == magic_number:
    print("So close!")
else:
    print("Way off!")

