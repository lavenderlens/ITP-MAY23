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
age = int(input())#no args
# age = input("SOCIAL MEDIA SURVEY: please enter your age >>>")#1 arg
# # somewhere in sytem code (built_ins)
# def input():
#     #TODO
#     pass
# # may or may not take an arg
# def input(message):
#     #TODO
#     pass

my_socials = ""
print("Do you use either of the following two social platforms: type Y for yes, any character for no")
if age < 21:
    print("TikTok? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += "TikTok, "
    print("SnapChat? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += "SnapChat, "
if age >= 21 and age <= 60:
    print("Facebook? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += "Facebook, "
    print("Twitter? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += "Twitter, "
if age > 60:
    print("MySpace? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += "MySpace, "
    print("Reddit? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials += "Reddit, "

# print(my_socials)#testing
print(f'You entered age {age} and use {my_socials}')