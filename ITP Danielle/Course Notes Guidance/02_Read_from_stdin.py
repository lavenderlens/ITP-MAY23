name = "Smith"
number = 433178878
balance = 250.70
is_taxable = True


name = input("Enter the account name: ")
number = int(input("Enter the account number: "))
balance = float(input("Enter the account opening balance: ")) #float as decimal points
is_taxable = bool(input("Enter the taxable status: True or False"))

#they are no longer strings so cannot output as strings

print("Name: " + name)
print("Number: " + number)
#TypeError: can only concatenate str (not "int") to str so amend to below
print("Number: " + str(number))
print("Balance: " + str(balance))
print("Is taxable?: " + str(is_taxable))