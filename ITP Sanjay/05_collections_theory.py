#the collection type we using in python is called a list
band = ("Patti", "Max", "Gary", "Soozie", "Stevie", "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy")

#lists are zero-indexed, have a length property which is writable

print(len(band)) #11

print (band [10]) #roy - 11th element

#we can add elements
band.append ("Alan")
print (band)
# updated length
print(len(band)) #12

#We can remove elements
# by direct index
del band [3]
print(band)

#by search using matching and index
print(band.index("Stevie")) # what position is Stevie at
del band[band.index("Stevie")]
print (band)

# so we want to disregard case (case insensitive)
print (band[0].upper())
print (band[0].lower())
print (band [0].casefold ())
print (band) #original unchanged by these methods

german = "das ist eine GROSSE tag"
print (german. lower())
print (german.casefold()) # very useful if working with language

#insert element by index - Kert Ramm after Jake
# find index of Jake
print(band.index("Jake"))
band.insert (6, "Kurt Ramm")
print(band)
# all subsequent elements are now previous index +1
# opposite is true for del (delete)

