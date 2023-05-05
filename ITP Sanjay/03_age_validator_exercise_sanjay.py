name= input ("Enter your name: ")
print("enter age")
age=int(input("Enter your age: "))
isvalid = (age>=18) and (age<=125)
print("age is: "+ str (isvalid))
# print("name is: "+ name)

# what if I wanted to print out the str and the int in one go?

print(f'{name} is {age} years old. Valid age? {isvalid}')

name= input ("Enter your name: ")
print("Enter your name: ")
name = input()
