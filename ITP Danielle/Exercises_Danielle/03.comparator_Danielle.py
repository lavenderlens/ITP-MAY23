num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1_Equals_Num2 = (num1 == num2)
print("Are the numbers equal?: " + str(num1_Equals_Num2)) 
# where num1 is 2 and num 2 is 2 result is True so code is working correctly
# where num1 is 2 and num2 is 4 the result is False so code is working correctly

num1_GreaterThan_Num2 = (num1 > num2)
print("First number is greater than the Second Number: " + str(num1_GreaterThan_Num2))
# where num1 is 2 and num2 is 4 result is false so code is working correctly as 2 is not greater than 4

num1_LessThan_Num2 = (num1 < num2)
print("First number is less than the second number: " + str(num1_LessThan_Num2))
# where num1 is 2 and num2 is 4 result is true so code is working correctly as 2 is less than 4
# ensure no stray / random brackets (that's why error was initially coming up)

#Condiitonal statement

# most common type of conditioanl statement is 'if else' 
# f strings - formatting a string - devise a conditional statement
# below is taken from 03.comparator exercise


print(f'is num1 greater than num 2? \n{num1 > num2}')

anothervar = 22 # added another variable to incorporate in the triple f string below

# triple f strings - as per below can be on separate lines 
# as long as you open brackets on the first line and close brackets on the last line.

print(f'''Question:
{anothervar}
is num1 less than num 2? 
{num1 < num2}''')

# old school way
print("Question:\n" 
+ str(anothervar) + "\n" +
"is num1 greater than num 2?\n"
+ str(num1 > num2))


# print(f'''is num1 equal to num 2? 
# {num1 == num2}''')

# print(type(num1))

# # if type(num1) == 'int': #OR
# if type(num1) == int:
#     print(f'{num1} is a number')


