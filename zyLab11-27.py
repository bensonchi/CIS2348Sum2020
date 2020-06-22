# Name:Baichuan Chi
# PSID:1938207


def print_menu():
    print()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')
    print('Choose an option:')


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

print_menu()
selection = input()
while selection != 'q':

    if selection == 'o':
        print('ROSTER')
        temp = list(rating_dict.keys())
        list_sorted = [int(i) for i in temp]
        list_sorted.sort()
        for jersey in list_sorted:
            print('Jersey number: {}, Rating: {}'.format(jersey, rating_dict[str(jersey)]))

    elif selection == 'a':
        jersey = input("Enter a new player's jersey number:\n")
        rating = input("Enter a new player's rating:\n")
        rating_dict[str(jersey)] = rating

    elif selection == 'd':
        jersey_delete = input('Enter a jersey number:\n')
        del rating_dict[jersey_delete]

    elif selection == 'u':
        jersey_update = input('Enter a jersey number:\n')
        rating_update = input('Enter a new rating for player:\n')
        rating_dict[jersey_update] = rating_update

    elif selection == 'r':
        min_rating = int(input('Enter a rating:\n'))
        print('ABOVE', min_rating)
        temp = list(rating_dict.keys())
        list_sorted = [int(i) for i in temp]
        list_sorted.sort()
        for jersey in jersey_sorted:
            if int(rating_dict[str(jersey)]) > min_rating:
                print('Jersey number: {}, Rating: {}'.format(jersey, rating_dict[str(jersey)]))
    else:
        print('Invalid entry')
    print_menu()
    selection = input()