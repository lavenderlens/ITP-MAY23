import random
magicnumber=random.randint(1,10)
print(magicnumber)
userguess = (int)(input("please guess the magic number between 1 and 10: "))
if userguess == magicnumber:
    print ("you have got it")
elif userguess +1 == magicnumber or userguess -1 == magicnumber:
    print ("so close")
else:
    print ("way off")    
