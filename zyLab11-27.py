# Name:Baichuan Chi
# PSID:1938207

rating_dict = {}

for i in range(1, 6):
    print("Enter player {}'s jersey number:".format(i))
    jersey = input()
    print("Enter player {}'s rating:".format(i))
    rating = input()
    rating_dict[jersey] = rating

print('ROSTER')
jersey_sorted = list(rating_dict.keys())
jersey_sorted.sort()

for jersey in jersey_sorted:
    print('Jersey number: {}, Rating: {}'.format(jersey, rating_dict[jersey]))