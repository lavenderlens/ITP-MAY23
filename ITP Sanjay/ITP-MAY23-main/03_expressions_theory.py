# an expression is a statement that yields a new value or result

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

print("# the NOT operator not")
myOriginal = False
print(not myOriginal)#True
print(myOriginal)#Original is still False
#page3-9
# ASSIGNMENT
