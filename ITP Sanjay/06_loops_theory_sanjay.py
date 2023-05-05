#loop is that repeats either for a counter, members of a collection
#or until the user does something or some condition changes

# counter
for x in range(1,6):# startIndex, endIndex - endIndex is EXCLUSIVE
    print(x)

    ingredients = ["chicken", "breadcrumbs", "salt", "garlic", "lemon", "rocket"]

    #looping round a collection
    for ingredient in ingredients:
        print (ingredient) # best practice single and plural nouns
    #ingredient is our made-up temporary variable name
    #ingredients is the actual name of an actual variable

# back to LHS margin when out of the loop

# looping round a collection using while with counter

print ("using while:")
counter = 0
while counter <len(ingredients):
    print(ingredients[counter])
    # must do is to increment the counter whilst do the loop
    counter +=1
    
