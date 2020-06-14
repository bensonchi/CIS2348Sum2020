# Name:Baichuan Chi
# PSID:1938207


def exact_change(user_total):
    num_dollars = int(user_total // 100)
    user_total -= num_dollars * 100
    num_quarters = int(user_total // 25)
    user_total -= num_quarters*25
    num_dimes = int(user_total // 10)
    user_total -= num_dimes*10
    num_nickels = int(user_total // 5)
    num_pennies = user_total - num_nickels*5
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


amount = int(input())
if amount <= 0:
    print('no change')
else:
    dollar, quarter, dime, nickel, penny = exact_change(amount)
    if dollar != 0:
        if dollar == 1:
            print('1 dollar')
        else:
            print(dollar, 'dollars')
    if quarter != 0:
        if quarter == 1:
            print('1 quarter')
        else:
            print(quarter, 'quarters')
    if dime != 0:
        if dime == 1:
            print('1 dime')
        else:
            print(dime, 'dimes')
    if nickel != 0:
        if nickel == 1:
            print('1 nickel')
        else:
            print(nickel, 'nickels')
    if penny != 0:
        if penny == 1:
            print('1 penny')
        else:
            print(penny, 'pennies')