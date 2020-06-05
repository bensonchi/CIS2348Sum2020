#Name:Baichuan Chi
#PSID:1938207
import math

print('Enter wall height (feet):')
height = int(input())
print('Enter wall width (feet):')
width = int(input())

paint = float(height*width/350)
cans = math.ceil(paint)

print('Wall area:',height*width,'square feet')
print('Paint needed:','{:.2f}'.format(paint),'gallons')
print('Cans needed:',cans,'can(s)\n')

print('Choose a color to paint the wall:')
color={'red':35,'blue':25,'green':23}
color_choice = input()
print('Cost of purchasing',color_choice,'paint: ${}'.format(cans*color[color_choice]))