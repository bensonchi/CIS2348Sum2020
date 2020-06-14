# Name:Baichuan Chi
# PSID:1938207

user_str = input()  # take user input
user_str_ns = user_str  # make copy for modification

space_pos = user_str_ns.find(' ')  # initiate a variable to represent the position of space in user_str
while space_pos != -1:  # remove all spaces in the string
    user_str_ns = user_str_ns[:space_pos]+user_str_ns[space_pos+1:]
    space_pos = user_str_ns.find(' ')

if len(user_str_ns) % 2 == 1:  # assign endpoint for our for loop below depending on the string is odd or even
    end = (len(user_str_ns)-1)/2
else:
    end = len(user_str_ns)/2

test = 1  # test = 1 if the character are equal and vice versa. We initialize it with 1
for i in range(0, int((len(user_str_ns)-1)/2)):
    if user_str_ns[i] != user_str_ns[-i-1]:
        test = 0
        break
print(user_str, 'is a palindrome') if test == 1 else print(user_str, 'is not a palindrome')
