myNumber = 42 #whole number
print(type(myNumber))#<class 'int'>
# a python comment - will not affect the code
# variables are placeholders for values
# in Python, there is NO KEYWORD to declare a variable
# it's just the name,
# when it pops up for the first time
# when it is not a system keyword,
# it must be initialised when first declared
# PY is a dynamically-typed language
# variables can and do change their types
# the type of a variable is inferred from the expression

myNumber = "forty-two" #reassigning
print(type(myNumber))#<class 'str'>

myNumber = 42.0 # changed back to numner (float)
print(type(myNumber))#<class 'float'>
myNumber = True
print(type(myNumber))#<class 'bool'> # boolean

myNumber = 42
#copying (pf reference)
myOtherNumber = myNumber + 1

#print value - don't use quotes as the output would be the exactly what the command is.
print(myNumber) #42 (output)
print(myOtherNumber) #43 (output)
print("myNumber") #myNumber (output)
print("myOtherNumber") #myOtherNumber (output)

#Ctrl D = multi-select
#Ctlr Shift Down Arrow - duplicate line

# indents and code blocks
def myFunction(): 
    print("I am inside the function")
    print("I am still inside the function")
#once loaded the function with def - do not need to define def again)

myFunction()
print("I am outside the function") 

#truthiness
# any value has an implicit true or false value as well
# this is called 'truthiness'
# we can check this by passing a value to the bool() constructor function(more of that later)
print(bool(1)) # true
print(bool(0)) # false
print(bool(-99)) # true 
# any non-zero number is intrinsically true)
print(bool("1")) # true
print(bool("0")) # true
print(bool("")) #false
# any non-empty number is intrinsically true)

#input from user
num1 = input("enter a number")
num2 = input("enter another number")
print(num1)
print(num2)
print(num1 + num2) #concatenation and is not mathematics adding them together

num3 = int(input("enter a number"))
num4 = int(input("enter another number"))
print(num3)
print(num4)
print(num3 + num4) # the number have been coerced from str type to int typ to allow for addition

num5 = float(input("enter a number"))
num6 = float(input("enter another number"))
print(num5)
print(num6)
print(num5 + num6)

name = 'Smith'
print(name)
age = 21
print(age)
print("Name: " + age) #ERROR
print("Name: " + str(age))

input_name = input("Enter some letter")
print(type(input_name))
input_number = float((input("Enter some digit characters)")))
print(type(input_number)
      )


