name = input("Enter the account name:")
number = int(input("Enter the account number"))
balance = float(input("Enter the account opening balance"))
is_taxable = bool(input("Enter the taxable status:"))

print("Name: " + name)
print("Number: " + str(number))
print ("Balance: " + str(balance))
print("Is taxable?: " + str(is_taxable))
