# Name:Baichuan Chi
# PSID:1938207

user_input = input()
tokens = user_input.split()

words = {}

for i in tokens:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

for i in tokens:
    print(i, words[i])
