# an expression is a statement that yields a new value or result
# expressions can be very complex
# but are said to evaluate to a single value
# for now, those values will be either
# str
# int
# float
# bool
# the last of these, boolean, is probably the most versatile
# even though it can only be only be one value or the other: True or False
# different operators (doing symbols) work on one or many operands (variables or values that represent data)
# the end result of an expression depends on what type of operators used
# arithmetic operators operate on numbers and evaluate to numbers
# relational operators operate on many operands and evaluate to boolean (True or false)
# they compare one operand to another
# logical operators operate on many operands and evaluate to boolean (True or false)
# they compare the truth value of one operand to another


result = 16 * 4
print(result)
#variable result holds the value of multiplying operand 16 by operand 4
# we can make expressions from other variables too

x = 16
y = 4

result = x * y
print(result)

# operator categories:

print("# ARITHMETIC")
print(x + y)#20
print(x - y)#12
print(x * y)#64
print(x / y)#4.0
print(x % y)#0

print("# RELATIONAL")
print(x == y)#False
print(x != y)#True
print(x > y)#True
print(x >= y)#True
print(x < y)#False
print(x <= y)#False


print("# LOGICAL")
my_true = True
my_false = False

print(my_true and my_false)#False #True when both sides True
print(my_true or my_false)#True #True when at least one side is True
print(my_true ^ my_false)#XOR #True when exactly one side is True and the other is False
print(True or True)#True
print(True ^ True)#False
print(True ^ False)#True

# logical operators work on truth values
# those truth values may be derived or worked out or evaluated
# from other expressions
x > y and y <= x
# becomes
True and True
# which evaluates to True

x > y and y >= x
# becomes
True and False
# which evaluates to False

x > y or y >= x
# becomes
True or False
# which evaluates to True

x < y or y >= x
# becomes
False or False
# also applies
False and False
# which evaluates to False either way

# think of expressions as puzzles for the code
# how do you solve a complex puzzle like a crossword?
# you break it down into parts eg rows, columns, letters
# similarly, the code only works out one thing at a time
# so complex expressions boil down to or evaluate as
# simpler expressions, and so on

# for example (manual)
# I wish to purchase a phone outright for under €500
# it must have
# two cameras
# and 5G capability
#  I can express this as follows:

cameras = 2
has5G = True
price = 450

canIPurchasePhone = cameras ==2 and has5G and price <= 500

# for the above expression to evaluate to True
# the LHS, middle, and RHS have to be True

print("cameras ==2 and has5G and price <= 500")
print(cameras ==2 and has5G and price <= 500)
print(canIPurchasePhone)



print("# the NOT operator not")
myOriginal = False
print(not myOriginal)#True
print(myOriginal)#Original is still False-
# this is called an immutable operation - original is unchanged
# if i wanted to change the value of myOriginal for good
# I combine the operator with a re-assignment step:
myOriginal = not myOriginal
print(myOriginal)
# this is called a mutable or mutating operation - the original is overwritten
# think of the difference between mutable and immutable
# as the difference between Save and Save As
# going forwards, but beyond the scope of this course,
# immutable methods of working with data
# are a huge core concept in data science

# ASSIGNMENT
# single =
x = 1
# the value 1 is assigned to the reference x
canIPurchasePhone = cameras ==2 and has5G and price <= 500
# the value of the expression is assigned to the ref canIPurchasePhone

# there exists compound assignment operators
# +=
# takes a vlue and adds it on to itself
x = x + 1
# value of x is now 2
# OR
x += 1
# value of x is now 3
# += is shorhand for saying add this to itself
#  doesn't need to be step of 1
x += 2
# value is 3 + 2 >>>> 5
#  -= same but subtracts
y =10
y -=3
# value of y is 7
# +=, like + on its own, works for strings too
s =""
s += "I "
s += "love "
s += "Python "
# value of s is now "I love Python"
# there are other compound operators - see table in manual
# use cases very rare

print("# OPERATOR PRECEDENCE\n")

#  we are to invite a certain no. of farmers to an agricultural show
# we use Python to write the invites
# invitationText = "No.of Farmers: " + str(10) + str(1)
# invitationText = str(10) + str(1) + " No.of Farmers."
invitationText = str(10 + 1) + " No.of Farmers."
print(invitationText)
# order of expressions is very imporatant
#  and brackets can control the order in which things get worked out

#  there is an order of precedence of operators
#  computers can only generally work out one thing ata time
# the order of precedence determines which operators get done first
# BODMAS or BOMDAS are school maths acronyms for
# brackets, 
# ordinals (raise number to power of 2 etc)
# multiply/divide (divide and multiply)
# addition, subtraction

print(1 + 2 * 3)#7
print((1 + 2) * 3)#9
# in the absence of any differing preferences
# code is evaluated in the expression from L to R
print(6/3*4)#8.0



