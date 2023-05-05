age = int(input("Enter age: "))
ageGreaterEqualto = age >= 18
print("Age is greater than or equal to 18: " + str(ageGreaterEqualto))
ageLessEqualto = age <= 125
print("Age is less than or equal to 125: " + str(ageLessEqualto))
isValid = age >= 18 and age <= 125
# isValid stores a True or False value, the result of the expression on RHS of the single =
print("Age is valid? " + str(isValid))


