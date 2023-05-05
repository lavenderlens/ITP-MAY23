#can use multiline comments in Python using ''' at the beginning and ''' at the end.

''' 
construct a survey using branching logic based on age
the survey is of social media platforms used
and presents a different set of questions for each age range
if age is under 21, the options are
    TikTok
    SnapChat
if between 21 - 60, options are
    Facebook
    Twitter
if over 60,
    MySpace
    Reddit
'''

print("SOCIAL MEDIA SURVEY: please enter your age >>>")
# age = input() # no arguments
# age = input("SOCIAL MEDIA SURVEY: please enter your age >>>") # 1 argument

age = int(input())

my_socials = "" #variable
print("Do you use either of the following two social platforms: Type Y for yes, any charater for No:")
if age < 21:
    print("Tiktok? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += " TikTok, "
    print("Snapchat? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += " Snapchat, "

if age >= 21 and age <= 60:
    print("Facebook? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += " Facebook, "
    print("Twitter? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += " Twitter, "

if age > 60:
    print("MySpace? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += " MySpace, "
    print("Reddit? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += " Reddit, "

print(my_socials)

#above coding tested and working

#print (mysocial_)#testing
print(f'You entered age {age} and use {my_socials}')
#output result is 'You entered age 56 and use Twitter'
