'''
a function is a group of one or more statements (LOC - lines of code)
grouped by a name
and defined by the keyword def
the name,
parameter brackets ()
optionally, with parameters inside (values, a copy of which is passed into the function)
and a colon
and indented one tab space, LOC
'''

#print("Hello")
#print("World")
#print("How are you today?")
#3 print statements in a row procedurally

# I may wish to group these in a function
#stag 1: define function
def greet():
    print("Hello")
    print("World")
    print("How are you today?")

#stage 2: call function
greet()

def greetInIrish():
    print("Cade e am ata tu")
    print("World")
    print("HGo maith!?")

greetInIrish()
