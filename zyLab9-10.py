# Name:Baichuan Chi
# PSID:1938207

import csv
file_name = input()
words = {}  # set up a dictionary to track words frequencies

with open(file_name, 'r') as file:  # open the csv file
    reader = csv.reader(file)

    for row in reader:
        for word in row:
            if word not in words.keys():  # check if the word has come up before or not
                words[word] = 1
            else:  # update the dictionary if the entry exists.
                words[word] += 1

for entry in words:  # print result
    print(entry, words[entry])