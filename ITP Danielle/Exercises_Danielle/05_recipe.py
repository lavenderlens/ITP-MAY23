ingredients = ["chicken", "breadcrumbs", "salt", "garlic", "lime"] # collection
print("ORIGINAL")

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

del ingredients [4] # delete lime
ingredients.append ("lemon") #lemon
ingredients.append ("rocket") #add rocket
del ingredients [2] #remove salt

print ("After Changes")
print(ingredients[0]) #chicken
print(ingredients[1]) #breadcrumbs
print(ingredients[2]) #garlic
print(ingredients[3]) #lemon
print(ingredients[4]) #rocket