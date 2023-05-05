print("Enter name: ")
print("Enter age: ")
age = int(input())

isValid = age >= 18 and age <= 125
print("Is the age greater than or equal to 18 and less than or equal to 125: " +str(isValid))
# where age is 21 result is true so code is working correctly as 21 falls within the range 18 - 125
# where age is 12 results is false so code is working correctly as 12 falls outside of



#additional notes going through exercise altogether

#1
print(name + '\'s age is' + str(age) + '\nValid?' + str(isValid))

# 2 Python 3 on
print('{}\'s age is {} \nValid? {}'.format(name, age, isValid))
# variable values get computed into string representations
# placeholders must be the right number and right order

# 3 Python 3.5 on ✅
print(f'{name}\'s age is {age} \nValid? {isValid}')
# placeholders can accept inline variables 
# # placeholders are {}


# 4 Python 3.7 on 
print(f'''
{name}\'s age is {age} 
Valid? {isValid}''') 
# very similar to JS template literals see below