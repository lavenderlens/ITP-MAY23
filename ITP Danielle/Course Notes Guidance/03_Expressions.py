#an expression is a statement that yields a new value or result i.e.
# expressions can be very complex
# but are said to evauate to a single value
# for now those values will be either
# str
# int
# float
# bool
# the last of these boolean, is probably the most versatile.
# even though it can only be one value or the other ie. True or False
# different operators (doing symbols) workon one or many operands (variables or values that represent data)
# the end result of an expression depends on what type of operators (symbols) are used
# think ot expresssions as puzzles for the code
# how do you solve a complex puzzle
# you break it down into parts e.g. rows, columns, letters
# similarly, the code only works out one thing at a time
# so complex expressions boil down to or evaluate as 
# simpler expressions and so on.

result = 16 * 4 # times is always * not x as we would wrtie it normally
print(result)
#variable result holds the value pf multiplying operand 16 by operand 4

#we can make expressions from other variables too i.e.

x = 16
y = 4

result = x * y
print(result)

#operator categories:

# arithmetic operators operate on numbers and evaluate to numbers

print("#ARITHMETIC")
print(x + y) #20
print(x - y) #12
print(x * y) #64
print(x / y) #4.0
print(x % y) #0

# Relational operators operate on many operands and evaluate to boolen (true or false). thye compare on operand to another
print("#RELATIONAL")
print(x == y) #equalled to # FALSE
print(x != y) # does not equal #TRUE
print(x > y) #TRUE
print(x >= y) #TRUE
print(x < y) #FALSE
print(x <= y) # FALSE

# Logical operators operate on many operands and evaluate to boolen (true or false). 
# They compare the truth value or one operand to another
print("#LOGICAL")
my_true = True
my_false = False

print(my_true and my_false)#False need two trues to make an and true / #TRUE when both sides TRUE
print(my_true or my_false)#True only need one true to make an or true / #TRUE when at least one side is TRUE
print(my_true ^ my_false)#True # ^ is an exclusive or (XOR) #TRUE when exactly one side is TRUE and the other is FALSE
print(my_true or my_true) #True
print(my_true ^ my_true) #False
print(my_true ^ my_false) # True

# logical operators work on truth values
# those truth values may be derived or worked out or evaluated
# from other expressions

x > y and y <= x
#becomes
True and True
# which evaluates to true

x > y and y >= x
#becomes
True and False
# which evaluates to false

x > y or y >= x
# becomes
True or False
#which evaluates to true only need one true to make a true for or)

x < y or y >= x
# becomes
False or False
# also applies 
False and False
# which evaluates to false either way


# for example
# I wish to purchase a phone outright for under £500
# it must have # two cameras
# # and 5g
# I can express this as follows:

no_of_cameras = 2
has_5g = True
price = 450

no_of_cameras ==2 and has_5g and price <= 500

# for the above expressoons to evaluate to True
# the left hand side, middle and right hand side have to be True.

print("no_of_cameras ==2 and has_5g and price <= 500")
print(no_of_cameras ==2 and has_5g and price <= 500)

# can turn above into a variable byt changin above the below:

CanIPurchasePhone = no_of_cameras ==2 and has_5g and price <= 500
# th output can then be:
print(CanIPurchasePhone)


# the Not operator ! is for Java but the word NOT has to be used for Python

my_original = False
print(not my_original) #True # called a urinery operand
print(my_original) # False #Original is still false
# this is called an immutable operation - oriigal is unchanged
# if i wanted to change the value of myOriginal for good
# I combine the operator with a re-assignment step

my_original = not my_original
print(my_original)
# this is called a mutable or mutating operation - the original is overwritten
# think of the difference between mutable and immutable
# as the difference between Save (mutable) and Save As (immutable)
# going foreards, but beyond the scope of this course
# immutable mehtods of wokring with data
# are a huge core concept in data science

#ASSIGNMENT
# single = 
x = 1
# the value 1 is assigned to the reference x
CanIPurchasePhone = no_of_cameras ==2 and has_5g and price <= 500
# the value of the expression is assigned to the ref CanIPurchasePhone

# there exists compound assignment operators
# += addition assignment
# takes a value and adds it onto itself
x =  x + 1
# value of x is now 2 due to 1 + 1
# OR
x += 1
# value of x is now 3 due to 2 + 1 (having changed the value of x)
# += is shorthand for saying add this to itself.
# doesn't need to be step of 1
x += 2
# value is 3 += 2
# value is 3 + 2 >>>>> 5

print("#OPERATOR PRECEDENCE\n") # \n denotes a new line after Operator Precedence

# we are to invite a certain number of farmers to an agricultural show
# we use python to write the invites
# invitationText = "No. of Farmers:" + str(10) + str(1)
# print(invitationText) #result is 101

invitationText = "No. of Farmers:" + str(10 + 1)
print(invitationText) #result is 11

# the order of prrecedence dtermines which operators get done first
# BODMAS or BOMDAS are school maths acronyms for 
# brackets, 
# ordinals (raise number to poweer of 2 etc
# multiply/divid (divie and multiply)
# addition, substraction

print(1 + 2 * 3) # 7 as multiplying is done first
print((1 + 2) * 3) #9
# in the absence of any differing preferences
# code is evaluated in the expression L to R

print(6/3*4) #8
#division get promoted to a float (deicmal)