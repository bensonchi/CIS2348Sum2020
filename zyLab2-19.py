#Name:Baichuan Chi
#PSID:1938207

print('Enter amount of lemon juice (in cups):')
lemon_juice = float(input())
print('Enter amount of water (in cups):')
water = float(input())
print('Enter amount of agave nectar (in cups):')
agave_nectar = float(input())
print('How many servings does this make?')
serving = float(input())
print()
print('Lemonade ingredients - yields','{:.2f}'.format(serving),'servings')
print('{:.2f}'.format(lemon_juice),'cup(s) lemon juice')
print('{:.2f}'.format(water),'cup(s) water')
print('{:.2f}'.format(agave_nectar),'cup(s) agave nectar')

print('\nHow many servings would you like to make?')
serving_needed = float(input())
print()
print('Lemonade ingredients - yields','{:.2f}'.format(serving_needed),'servings')
print('{:.2f}'.format(serving_needed/serving*lemon_juice),'cup(s) lemon juice')
print('{:.2f}'.format(serving_needed/serving*water),'cup(s) water')
print('{:.2f}'.format(serving_needed/serving*agave_nectar),'cup(s) agave nectar')

print('\nLemonade ingredients - yields','{:.2f}'.format(serving_needed),'servings')
print('{:.2f}'.format(serving_needed/serving*lemon_juice/16),'gallon(s) lemon juice')
print('{:.2f}'.format(serving_needed/serving*water/16),'gallon(s) water')
print('{:.2f}'.format(serving_needed/serving*agave_nectar/16),'gallon(s) agave nectar')