'''
collections store bunches of values
those values themselves may be complex i.e. other collections
a aocllection has a referecne variable name
it has elements
it has indices
use cases: collections are everywhere
The DVLA maintains a collection of millions of driver details
Having data in a collection, together
means we can ask different questions of the data
each question returning a different subset of the data
or a transformed copy of the data
Currys/PC World
Go on to webs toe
search for laptops
cry small tears when you see the prices
collection is probably ordered highest price first or popularity
apply filters for Acer manufacturer and order: lowest price first
breathe sigh of relief
collections are centrl to the user asking for diffferent views of the data

learning objectives:
leane how to declare a collection
learn how to add / delete elements
learn hot to get / set elements (reading of writing to individuals indices)
'''
#the collection type we are using in Pyhton is called list

band = ["Patti", "Max", "Gary", "Soozie", "Stevie"]

# lists are zero-indexed, have a lengthy propertuy which is writable.

print(len(band)) # no of names # 5
#print(band[5]) # Index Error: list index out of range
print(band[4]) #Stevie (is the 4th element as starts from 0 not 1)
print(band[0]) #Patti

#we can chnage /modify elements in a list i.e. chnage name to full name not just forename
band[0] = "Patti Scialfi"
band[4] = "Stevie Trooper"
print(band[4]) #Stevie Trooper
print(band[0]) #Patti Scialfi

#we can add elements:
band.append('Alan') #original changed by these methods
print(band)
#updated length
print(len(band)) # 0-5 now not 0-4

#we can remove elements
#by direct index
del band[3] #original changed by these methods
print(band)

#this changes the band by removing element 3 'Soozie'
#from ['Patti Scialfi', 'Max', 'Gary', 'Soozie', 'Stevie Trooper', 'Alan']
#to ['Patti Scialfi', 'Max', 'Gary', 'Stevie Trooper', 'Alan']

#by search
print(band.index("Stevie")) # what position is Stevie at
del band[band.index("Stevie")] # this obtains the index value for the index Stevie
print(band)
#original changed by these methods

#so if we want to disregard case (case sensitive)
print(band[0].upper())
print(band[0].lower())
print(band[0].casefold())
print(band)#original unchanged by these methods


#insert element by index