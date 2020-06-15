# Name:Baichuan Chi
# PSID:1938207

# set up a dictionary to match month word with number
month_num = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7',
             'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}

with open('inputDates.txt', 'r') as f:  # open file for read
    with open('parsedDates.txt', 'w') as w:  # open file or create file for write
        for line in f:
            if line == '-1':
                break
            elif '.' in line:  # ignore entries that includes  abbrev like 'Nov.')
                continue
            elif 'A' <= line[0] <= 'Z':
                user_split = line.split(', ')
                month_day, year = user_split[0], user_split[1]
                month_split = month_day.split(' ')
                month, day = month_num[month_split[0]], month_split[1]
                w.write('{}/{}/{}'.format(month, day, year))  # modified to write to file instead of print screen
            else:
                continue
