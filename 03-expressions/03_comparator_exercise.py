print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())
num1EqualNum2 = num1 == num2
print("The numbers are equal: " + str(num1EqualNum2))
num1GreaterThanNum2 = num1 > num2
print("The first number is greater than the second: " + str(num1GreaterThanNum2))
num1LessThanNum2 = num1 < num2
# print("The first number is less than the second: " + str(num1LessThanNum2))
print(f"The first number is less than the second: {num1 < num2}")

print(f'is num1 greater than num 2? \n{num1 > num2}')
anotherVar = 22
# triple f strings
print(f'''Question:
{anotherVar}
is num1 greater than num 2? 
{num1 > num2}''')
      
    #   old-school way:
print("Question:\n"
+ str(anotherVar) + "\n" +
"is num1 greater than num 2?\n" 
+ str(num1 > num2))

