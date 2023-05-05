#Conditional statement

# most common type of conditional statement is 'if else' 
# f strings - formatting a string - devise a conditional statement
# so far all the programs written comprise of a single path where each instruction is executed in sequence.

# a conditional statment respresents a decision after which the program flows along one of two or more possible paths.
# a program flow statement which goes one way or another
# depednig on a boolean expression 
# if true something is executed, if dfalse something else is executed)

# Learnig outcomes:
# write if - elif - else statements
# write and understand our first CODE BLCOKS
# - indents from the left margin

# one branch decisions / conditional
# a colon will cause an indent on the next line
# this means this statement belongs to this condition and reliant upon the condition
if True:
    print('IF block in one branch executed')
    print('second line')

# the below which is not indented will be carried out regardless of the above
# and does not belong to the if True condiiton above
print('Carrying on as usual 1')

# two branches
if False:
    print('IF block in second branch executed')
    print('second line')
else:
    print('Code in ELSE block exeucted')

print('Carrying on as usual 2')

# three or more branches
if False:   
    print('IF block in there or more branches executed')
    print('second line')
elif True:
    print('Code in ELIF executed')
else:
    print('Code in ELSE block executed')

# N.B. else doesn't have a condition on it liek the if True condiition (anything else)
# N.B. other languages note elseif but python uses elif
print('Carrying on as usual 3')

# nested if statements
# where an else may have its own if - elif - else
# familiarity with Excel - used a lot in formulae/macros
# in coding, this is generally but not without eception, seen as less readable

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
else:
    if age < 65:
        print("Your are working age")
    else:
        print("You are retirment age")

# if confifent with python and idents re the indents belonging to the else
# would be better written

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 65: 
    print("Your are working age")
else:
    print("You are retirment age")

print("#ternary operator")
# a bit like an if else in one line
lightSwitch = "off" # this is overwritten by the below
light = 0
# light is on: 1
# light is off: 0

# <variable> =  <value> if  <condition> else <value>

lightSwitch = "on" if light == 1 else "off"
#forced choice, used in situations where you can't have two trues or two falses
# decision must be one thing or another - exclusive OR ^

