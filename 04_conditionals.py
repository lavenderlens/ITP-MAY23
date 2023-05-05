# what is a conditional
# a program flow statement which goes one way or another
# depending on a boolean expression


# learning outcomes: you will be able to:
# write if - elif - else statements
# write and understand our first CODE BLOCKS
# - indents from the left margin

# one branch decision/conditional
if False:
    print('IF block in one branch executed')
    print('second line')

print('Carrying on as usual 1')

# two branches 
if False:
    print('IF block in two branch executed')
    print('second line')
else:
    print('Code in ELSE block executed')

print('Carrying on as usual 2')

# three or more branches 
if False:
    print('IF block in three or more branches executed')
    print('second line')
elif True:
    print('Code in ELIF block executed')
else:
    print('Code in ELSE block executed')

print('Carrying on as usual 3')

# in the morning backlog
# go through this again with real world example
# survey example
# suppress VSC popups!!

# nested if statements
# where an else may have it's own if - elif - else
# familiarity with Excel - these are used a lot in formulae/macros
# in coding, this is generally but not without exception, seen as less readable

age = int(input("Enter your age:"))

if age < 18:
    print("You are a minor")
else:
    if age < 65:
        print("You are working age")
    else:
        print('You are retirement age')

# probaly more readable:

if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 65:
    print("You are working age")
else:
    print('You are retirement age')

print("# ternary operator")
# a bit like an if else in one line
lightSwitch = "off"
light = 0
# light is on: 1
# light is off: 0
# <variable> = <value> if <condition> else <value>
lightSwitch = "on" if light == 1 else "off"
# forced choice, used in situations where you can't have two trues or two falses
# decision must be one thing or another - exclusive OR