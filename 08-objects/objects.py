# an object is a container or wrapper data structure
# it may have several parts
#  it may have object state - variables
#   and object behviour - functions

#object literal (dictionary in Python)
alan = {"name":"Alan", "Age":55, "Instruments": ["trombone", "keyborads","vox"]}
print(alan)

tom = {"firstName":"Tom", "lastname": "Morello","Age":65, "Instruments": ["guitar", "screwdriver"]}
print(alan)

# class Musician:
#     #constructor
#     def __init__(self):
#         self.name = 'Musician'
#         self.age = 0
#         self.instruments = []

# soozie = Musician()
# print(soozie)

class Musician:
    #constructor
    def __init__(self, name, age, instruments):
        self.name = name
        self.age = age
        self.instruments = instruments
    #other functions
    def printAll(self):
        # using f-strings and placeholders
        return f'Musician {self.name} is {self.age} years old and plays {self.instruments}'

soozie = Musician("Soozie Tyrell", 55, ["violin", "backing vox"])
print(soozie.printAll())
jake = Musician("Jarod Clements", 40, ["sax", "percussion"])
print(jake)#memory ref
print(jake.name)
jake.name = "Jake"
print(jake.name)
# objects are by default mutable whereas values are not

# pass by reference / pass by value
# number value
x = 1

def changeIt(number):
    number += 1
   
changeIt(x)
print(x)#values are immutable

def changeItObj(musician):
    musician.name = 'Alan'

changeItObj(soozie)
print(soozie.name)

jakeCopy = jake
#no new object just two references to same one
jakeCopy.name = "Jarod"
print(jakeCopy.name)
print(jake.name)
print(jake)#<__main__.Musician object at 0x103b679b0>
print(jake.printAll())
