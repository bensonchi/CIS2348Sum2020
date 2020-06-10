# Name:Baichuan Chi
# PSID:1938207

user_input = input()
for char in user_input:
    if char == 'i':
        char = '!'
    elif char == 'a':
        char = '@'
    elif char == 'm':
        char = 'M'
    elif char == 'B':
        char = '8'
    elif char == 'o':
        char = '.'
    print(char,end='')
print('q*s')