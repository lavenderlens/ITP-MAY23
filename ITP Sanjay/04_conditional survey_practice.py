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
age = int(input())# no arguments
# age = input("SOCIAL MEDIA SURVEY: please enter your age >>>")# 1 arg
my_socials ="" #variable
print ("Do you use either of the following two social platforms: type Y for yes, any character for N")
if age <21:
    print("TikTok Y/N")
    answer = input ()
    if answer.upper() =="Y":
        my_socials += "TikTok, "
    print("Snapchat Y/N")
    answer = input ()
    if answer.upper() =="Y":
        my_socials += "Snapchat, "

if age >=21 and age <=60:
    print("Facebook Y/N")
    answer = input ()
    if answer.upper() =="Y":
        my_socials += "Facebook, "
    print("Twitter Y/N")
    answer = input ()
    if answer.upper() =="Y":
        my_socials += "Twitter, "

print(my_socials)
