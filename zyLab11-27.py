# Name:Baichuan Chi
# PSID:1938207


def print_menu():
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')
    return input('Choose an option:\n')


rating_dict = {}

for i in range(1, 6):
    print("Enter player {}'s jersey number:".format(i))
    jersey = input()
    print("Enter player {}'s rating:".format(i))
    rating = input()
    rating_dict[jersey] = rating
    print()

print('ROSTER')
temp_list = list(rating_dict.keys())
jersey_sorted = [int(i) for i in temp_list]
jersey_sorted.sort()

for jersey in jersey_sorted:
    print('Jersey number: {}, Rating: {}'.format(jersey, rating_dict[str(jersey)]))

print()  # blank line to format the result to fit zyLab test

selection = print_menu()
while selection != 'q':

    if selection == 'o':
        print('\nROSTER')
        jersey_sorted = list(rating_dict.keys())
        jersey_sorted.sort()
        for jersey in jersey_sorted:
            print('Jersey number: {}, Rating: {}'.format(jersey, rating_dict[jersey]))

    elif selection == 'a':
        jersey = input("Enter a new player's jersey number:\n")
        rating = input("Enter a new player's rating:\n")
        rating_dict[jersey] = rating

    elif selection == 'd':
        jersey_delete = input('Enter a jersey number:\n')
        rating_dict.pop(jersey_delete)

    elif selection == 'u':
        jersey_update = input('Enter a jersey number:\n')
        rating_update = input('Enter a new rating for player:\n')
        rating_dict[jersey_update] = rating_update

    elif selection == 'r':
        min_rating = int(input('Enter a rating:\n'))
        print('ABOVE', min_rating)
        for (jersey, rating) in rating_dict.items():
            if int(rating)> min_rating:
                print('Jersey number: {}, Rating: {}'.format(jersey, rating))
        print()
    else:
        print('Invalid entry')

    selection = print_menu()