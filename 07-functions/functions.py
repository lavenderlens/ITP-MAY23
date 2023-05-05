# a function is a group of one or more statements 
# which can be invoked one or more times at a later date
# how small can a function be?
#  one line
#  how big can a function be?
#  suggest that of over 50 lines or thereabouts
# the function is a candidate for different smaller functions

# functions should be idempotent (see below)
# really long functions (>50 lines) are more likely to have dependencies
# readability concerns too are best addressed through smaller functions

myName = 'Alan'
def greet():
    print("Hello " + myName)
greet()

myName = 'Maktoum' # output has changed, function has not changed
greet()

# thi function is pure
# no dependencies
# passes in an argument by copy
def greetPure(name):
    print("Hello " + name)

greetPure('Lucas')

# functions can have:
# input
# output
# none
# or both

# output as in print to stdout is not considered output from a function
# output from a function is when the return keyword is used
# this means that the return value may be passed on / persisted in memory 
# to other parts of the app

# candidate statements for a function?
print('Hello')
print('World')
print('How are you?')

# 1. no input, no output
# def greet():
#     print('Hello')
# print('World')
# print('How are you?')
def greet():
    print('Hello')
    print('World')
    print('How are you?')

greet()

# 2. no input, with output (return statement)
def greet2():
    return 'Hello #2 World How are you?'

greet2()#output may be persisted but is not visible here
# way 1 - persist to another variable
greet2output = greet2()
print(greet2output)
# way 2 - pass output from greet2() as input to print()
print(greet2())

# return statement rules: 
# return statement should be LAST in function 
# we can have multiple return statements in one function 
# but EACH rtn stmt represents ONE path through the function
# happy path and sad path are terms used informally
# return statement should have as value a single expression

# 3. input AND output
# def greet3(name):#name is a parameter here at function definition time: generic
#     return 'Hello ' + name + ' how are you today?'
def greet3(name):#name is a parameter here at function definition time: generic
    return f'Hello {name} how are you today?'#fix for other (wrong?) datatypes


# greet3()#TypeError: greet3() missing 1 required positional argument: 'name'
print(greet3('Alan'))# name here is an argument: specific data at run time

# 4. output, but no input
def greet4():#name is a parameter here at function definition time: generic
    return 'Hello World how are you today?'
print(greet4())

print(greet3(123))#TypeError: can only concatenate str (not "int") to str

#pure vs impure
# all the above are pure functions
# pure functions have no external dependencies
# for given input, they will return the same output
# every time

# impure function:
# has a dependency as a global var
# may be overwritten 
# by circumstances outside the function
# an example of an impure function would be:
 
myName = "Clarence"
def greetNameImpure():
    return f'Hello {myName}'#pass  by reference

print(greetNameImpure())#Hello Clarence
myName = 'Jake'
print(greetNameImpure())#Hello Jake
# the function's output has been affected
# by a change in an external dependency

# pure function
def greetNamePure(name):
    return f'Hello {name}'

print(greetNamePure("Kurt"))
#always the same output 
# for the same input

#mutability
band = ["Bruce", "Patti", "Max", "Gary", "Soozie", "Stevie", "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

# a pure, IMMUTABLE filter function would be
def filterImmutable(list):
    # local variable - a new list
    filteredList = []
    for member in list:
        if len(member) <=4:
            filteredList.append(member)
    return filteredList

#original is unchanged
# a new list is returned 
# with just those members 4 letters or less
# a transformation has taken place

#testing
shortnames = filterImmutable(band)
print(shortnames)#['Max', 'Gary', 'Nils', 'Tom', 'Jake', 'Roy']
print(band)#unchanged

# see also file mutability.py for differences between the for and while loops