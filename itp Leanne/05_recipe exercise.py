ingredients = ["chicken", "breadcrumbs", "salt", "garlic", "lime"]
print(ingredients)
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

ingredients[4] = "lemon"
print(ingredients)

ingredients.append("rocket")
print(ingredients)

del ingredients[2]
print(ingredients)

print("AFTER CHANGES")
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

