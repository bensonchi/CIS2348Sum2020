# Name:Baichuan Chi
# PSID:1938207

user_input = input()
tokens = user_input.split()

nums = []

for i in tokens:

    if int(i) >= 0:
        nums.append(int(i))

nums.sort()
for i in nums:
    print(i, end=' ')