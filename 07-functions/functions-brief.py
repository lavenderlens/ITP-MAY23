'''
a function is a group of one or maore statements (LOC - lines of code)
grouped by a name
and defined by the keyword def,
the name,
parameter brackets ()
optionally, with parameters inside (values, a copy of which is passed into the function)
and a colon
and, indented one tab space, LOC
'''

# print("Hello")
# print("World")
# print("How are you today")
# 3 print statements in a row, procedurally

# I may wish to group these in a function
# stage 1 define function
def greet():
    print("Hello")
    print("World")
    print("How are you today")
#stage 2 call function
greet()

def greetInIrish():
    print("Cad é mar ata tú")
    print("Domhan")
    print("Go maith?")

greetInIrish()

def greetName(name):
    print("Hello")
    print(name)
    print("How are you today")

# greetName()#TypeError: greetName() missing 1 required positional argument: 'name'
greetName("Alan")

# TODO- return statements, output as input (to other functions)

