#Name:Baichuan Chi
#PSID:1938207

print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

service = {'Oil change':35,'Tire rotation':19,'Car wash':7,'Car wax':12,'No service':0}

print('Select first service:')
first = input()
if first=='-':
    first = 'No service'
print('Select second service:')
second = input()
if second=='-':
    second = 'No service'

print('\nDavy\'s auto shop invoice')
print()
if first == 'No service':
    print('Service 1: {}'.format(first))
else:
    print('Service 1: {}, ${}'.format(first, service[first]))
if second == 'No service':
    print('Service 2: {}'.format(second))
else:
    print('Service 2: {}, ${}'.format(second, service[second]))
print()
print('Total: ${}'.format(service[first]+service[second]))
