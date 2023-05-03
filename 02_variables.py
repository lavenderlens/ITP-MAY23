myNumber = 42 # whole number
print(type(myNumber))#<class 'int'>
# a python comment - will not affect the code
# variables are placeholders for values
# in Python, there is NO KEYWORD to declare a variable
# it's just the name, 
    # when it pops up for the first time
    # when it is not a system keyword
# it must be initialised when first declared
# PY is a dynamically-typed language
# variables can and do change their types
# the type of a variable is inferred from the expression
myNumber = "forty-two"#re-assigning
print(type(myNumber))#<class 'str'>
myNumber = 42.0#changed back to number (float)
print(type(myNumber))#<class 'float'>
myNumber = True
print(type(myNumber))#<class 'bool'>

myNumber = 42
#copying (of reference)
myOtherNumber = myNumber + 1

#print value
print(myNumber)#42
print(myOtherNumber)#43
print("myNumber")#myNumber
print("myOtherNumber")#myOtherNumber

# indents and code blocks
def myFunction():
    print("I am inside the function")
    print("I am still inside the function")

myFunction()
print("I am outside the function again")
myFunction()

# truthiness
# any value has an implicit true or false value as well
# this is called "truthiness"
# we can check this by passing a vlue to the bool() constructor function (more of that leter)
print(bool(-99))#True
print(bool(0))#False
# any non-zero number is intrinsically True
print(bool('1'))#True
print(bool('0'))#True
print(bool(''))#False

# any non-empty string is intrinsically True

# input from user
# num1 = input("enter a number")
# num2 = input("enter another number")
# print(num1)
# print(num2)
# print(num1 + num2)#concatenation

# num3 = int(input("enter a number"))
# num4 = int(input("enter another number"))
# print(num3)
# print(num4)
# print(num3 + num4)#4 - the numbers have been coerced from str type to int type

# num5 = float(input("enter a number"))
# num6 = float(input("enter another number"))
# print(num5)
# print(num6)
# print(num5 + num6)#4 - the numbers have been coerced from str type to int type

name = 'Smith'
print(name)
age = 21
print(age)
print("Name: " + name)
# print("Age: " + age)#ERROR
print("Age: " + str(age))

input_name = input("Enter some letters")
print(type(input_name))
input_number = float(input("Enter some digit characters"))
print(type(input_number))

