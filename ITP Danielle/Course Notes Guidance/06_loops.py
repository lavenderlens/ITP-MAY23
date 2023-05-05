# an iterative statement is one that allows for the repition of some instructions 
# a given number of times
# also known as loops 
# dependant upon a decision (boolean), 
# the results of which determines if the sintruction should be repeated
# two principle types "for" and "while" 
# typically described as "the for loop" and "the while eloop"

'''
starting with the collection (ingredients list) form our last exercise
lets do some loops or iterative statement which repates either for
- a counter
- member of a collections
- or until the users does something / some conditions changes e.g. end of file reached

learning outcomes:
- declare the two types of loop "for" and "while" loop
- use break and continue statements to exit/skip iterations
'''

#counter
for x in range(1,6): #startIndex, endIndex -endIndex is EXCLUSIVE
    print(x)#1-5

ingredients = ["chicken", "breadcrumbs", "salt", "garlic", "lemon", "rocket"] # collectio

#looping round a collection
for ingredient in ingredients: 
    print(ingredient) #best
# back to the LHS margin when out of the loop
# single term ingredient could be any word and is our made up temporary variable name
# but "ingredients" is the actual name of an actual variable
# if you were to use x instead of a word as the made up temporary variable
# x would be a hyoer-local variable parametised - 
# exists for long enouhg while the loop run 
# therefore no clash

#looping round a collection using while with counter
print("using while")
counter = 0 
# 0 is essentially chicken so telling the program to loop background from the beginning
while counter < len(ingredients): # len is #5
    print(ingredients[counter]) 
    #MUST do!!
    counter += 1

#looping an activity using while, no counter
print("using while with break")
guest_list = "" 
# 0 is essentially chicken so telling the program to loop background from the beginning
while True:
    name = input("Enter a name for the guest list, or x to quit")
    if name.lower() == "x":
        break
    guest_list += name + ", "

print(guest_list)

print("#using  break a in a for loop")
for x in ingredients:
    if x.lower() == 'garlic':
        break
    print(x)

print("using continue in a for loop")
for x in ingredients:
    if x.lower() == 'garlic':
        continue
    print(x)
