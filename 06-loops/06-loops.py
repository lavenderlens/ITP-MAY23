'''
starting with the collection (ingredients list) from our last exercise, let's do some loops
a loop, or iterative statement, is on ethat repeats, eithr for
    - a counter
    - members of a collection
    - OR, until the user does something, or some condition changes e.g. end of file reached

    learning outcomes:
    - declare the two types of loop:
        - for loop
        - while loop
    - use break and continue statements to exit/skip iterations
'''

# counter
for x in range(1,6):#startIndex, endIndex - endIndex is EXCLUSIVE
    print(x)#1-5

ingredients = ["chicken", "breadcrumbs", "salt", "garlic", "lemon", "rocket"]

# looping round a collection using for
for x in ingredients:
    print(x)#best practice single and plural nouns
# "ingredient" is our made-up, temporary variable name
#  "ingredients" is the actual name of an actual variable
#  "x" is a hyper-local variable:
# parameterised - exists only long enough while the loop runs
# therefore there is no clash with similarly-named parameterised variables

# back to LHS margin when out of the loop

# looping round a collection using while with counter
print("using while:")
counter = 0
while counter < len(ingredients):
    print(ingredients[counter])
    # MUST do!!
    counter += 1

# looping an activity using while, no counter
print("using while with break:")
guest_list = ""
# while True:
#     name = input("Enter a name for the guest list, or x to quit")
#     if name.lower() == "x":
#         break
#     guest_list += name + ", "

print(guest_list)

print("# using break in a for loop")
for x in ingredients:
    if x.lower() == 'garlic':
        break
    print(x)

print("# using continue in a for loop")
for x in ingredients:
    if x.lower() == 'garlic':
        continue
    print(x)




