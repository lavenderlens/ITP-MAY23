name = input("Enter the account name:")
number = int(input("Enter the account number:"))
balance = float(input("Enter the account opening balance"))
is_taxable = bool(input("Enter the taxable status: True or False"))

print("Name: " + name)
# print("Number: " + number)#TypeError: can only concatenate str (not "int") to str
print("Number: " + str(number))#TypeError: can only concatenate str (not "int") to str
print("Balance: " + str(balance))
print("Is taxable?: " + str(is_taxable))