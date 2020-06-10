# Name:Baichuan Chi
# PSID:1938207

# a1*x+b1*y=c1
# a2*x+b2*y=c2
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())


result1 = 0
result2 = 0
for x in range(-10, 11):
    for y in range(-10, 11):
        result1 = a1*x+b1*y
        result2 = a2*x+b2*y
        if result1 == c1 and result2 == c2:
            print(x, y)
            break
    if result1 == c1 and result2 == c2:
        break

else:
    print('No solution')