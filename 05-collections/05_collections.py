'''
collections store bunches of values
those values themselves may be complex ie. other collections
a collection has a reference variable name
it has elements
it has indices
use cases: collections are everywhere
The DVLA maintains a collection of millions of driver details
Having data in collection, together
means we can ask different questions of the data
each question returning a different subset of the data
or, a transformed copy of the data
Currys/PC World
Go on to web site
search for laptops
cry small tears when you see the prices
collection is probably ordered highest price first or popularity
apply filters for Acer manufacturer and order: lowest priced first
breathe sigh of relief
collections are central to the user asking for different views of the data

learning objectives for this section:
learn how to declare a collection
learn how to add / delete elements
learn how to get / set elements (reading or writing to individual indices)
'''

#the collection type we are using in Python is called list
band = ["Patti", "Max", "Gary", "Soozie", "Stevie", "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

# lists are zero-indexed, have a length property which is writable

print(len(band))#11

# print(band[11])#IndexError: list index out of range

print(band[10])#Roy - 11th element
print(band[0])#Patti - first element

# we can change / modify elements in a list
band[0] = "Patti Scialfa"
print(band[0])#Patti Scialfa - first element
band[10] = "Roy Bittan"
print(band[10])#

# we can add elements
band.append('Alan')#original changed by this method
print(band)
# updated length
print(len(band))#12

# we can remove elements
# by direct index
del band[3]#original changed by this method
print(band)
# by search
print(band.index("Stevie"))#what position is Stevie at 
del band[band.index("Stevie")]
print(band)

# so we want to disregard case (case insensitive)
print(band[0].upper())
print(band[0].lower())
print(band[0].casefold())
print(band)#original unchanged by these methods
# ß
german = "Das ist eine GROSSE tag"
print(german.lower())

german = "Das ist eine GROßE tag"
print(german.lower())
print(german.casefold())#VERY useful if working with language-specific locales

# insert element by index - Kurt Ramm after Jake
# find index of jake
print(band.index("Jake"))
band.insert(6, "Kurt Ramm")
print(band)
# all subsequent elements are now previous index + 1
# opposite is true for del (delete)



