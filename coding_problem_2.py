# Name:Baichuan Chi
# PSID:1938207

# set up a dictionary to match month word with number
month_num = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7',
             'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}
user_date = input('Please enter a date in the format of \'March 1, 1990\'')
if user_date != '-1':
    user_split = user_date.split(',')
    month_day, year = user_split[0], user_split[1]
    month_split = month_day.split(' ')
    month, day = month_num[month_split[0]], month_split[1]
    print('{}/{}/{}'.format(month, day, year))
else:
    print('Thank you')