# Name:Baichuan Chi
# PSID:1938207
from datetime import datetime

# Welcome message
print('Welcome to Birthday Calculator!\n')

# prompt user for input
today = datetime.strptime(input('Please enter the current date in the form of mm/dd/yy: '), '%m/%d/%y')
birthday = datetime.strptime(input('Please enter your birthday in the form of mm/dd/yy: '), '%m/%d/%y')

# age is the difference between birth year and current year
age = int(today.year - birthday.year)

# age need to -1 if the person hasn't reach current year's birthday
if (today.month, today.day) < (birthday.month, birthday.day):
    age -= 1

# output result
print()
print('==============================')
print('==Birthday Calculator Result==')
print('==============================')
print('Current Day')
print('Month:', today.month)
print('Day:', today.day)
print('Year:', today.year)
print()
print('Birthday')
print('Month:', birthday.month)
print('Day:', birthday.day)
print('Year:', birthday.year)
print('You are',age,'years old.')
print()
# check if the person's birthday is today
if (today.month, today.day) == (birthday.month, birthday.day):

    print('It\'s your birthday today! Happy birthday!')
