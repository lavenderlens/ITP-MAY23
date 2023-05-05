ingredients = ["chicken", "breadcrumbs", "salt", "garlic", "lime"]
print ("original")
print (ingredients[0]) # chicken
print (ingredients[1]) # breadcrumbs
print (ingredients[2]) # salt
print (ingredients[3]) # garlic
print (ingredients[4]) # lime

del ingredients [4] #delete lime
ingredients.append ("lemon")
ingredients.append ("rocket")
del ingredients [2] #delete salt

print ("After Changes")
print (ingredients[0]) # chicken
print (ingredients[1]) # breadcrumbs
print (ingredients[2]) # rocket
print (ingredients[3]) # garlic
print (ingredients[4]) # lemon

