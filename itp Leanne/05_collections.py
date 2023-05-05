band = ["Patti", "Max", "Gary", "Soozie", "Stevie", "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

print(len(band))

print(band[10])
print(band[0])

band[0] = "Patti Scialfa"
print(band[0])
band[10] = "Roy Bittan"
print(band[10])

band.append('Alan')
print(band)

print(len(band))

del band[3]
print(band)

print(band.index("Stevie"))
del band[3] 
#or 
del band[band.index("Stevie")]
print(band)

print(band[0].upper())
print(band[0].lower())
print(band[0].casefold())

german = "Das ist eine GROSSE tag"
print(german.lower()) #casefold for German double upper S

print(band.index("Jake"))
band.insert(6, "Kurt Ramm")
print(band)
