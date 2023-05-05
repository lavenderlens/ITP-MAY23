# design an app that will
# take a mark percentage 1-100
# output a grade A-C
# A grade is 80-100
# B grade is 60-79
# C grade is 59 or under

mark = int(input("Enter your mark 1-100"))
grade = ""
if mark >= 80:
    grade = "A"
elif mark >= 60:
    grade = "B"
elif mark <= 59:
    grade = "C"
else:
    grade = "N/A"
print("your grade was " + grade + ": Goodbye")