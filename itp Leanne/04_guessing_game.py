import random
magicNumber = random.randint(1,10)
guess = int(input("Guess the magic number between 1 and 10: "))
if guess == magicNumber:    
    print("WINNER!!! You guessed it right!")
elif guess + 1 == magicNumber or guess - 1 == magicNumber:
    print("Close, but wrong!")
else:
    print("Way off, LOSER!!")
print(f'''
The magic number is:
{magicNumber}
''')