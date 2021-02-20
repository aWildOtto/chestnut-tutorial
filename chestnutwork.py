# Mixing color
# Ask the user to input one of the three primary colors: red, yellow, and blue. 
# Ask for a second primary color. 
# If the user answer incorrectly, prompt the user to try again. 
# Combine these two colors and give the user an output. 
# (red + yellow = orange; red + blue = purple; yellow + blue = green)

# Sample output:
# Hello, welcome to our color mixing program!
# Give me one primary color
# Green
# Sorry, green is not a primary color, try again!
# Yellow
# Great! Could you give me a second primary color? 
# Blue 
# Awesome! 
# yellow plus blue is green

print('Hello, welcome to our color mixing program!')
first = input('Give me one primary color\n').lower()

while first != 'red' and first != 'yellow' and first != 'blue':
    print('Sorry, {} is not a primary color, try again!'.format(first))
    first = input('Give me one primary color\n').lower()
print('Great!', end=' ')

second = input('Could you give me a second primary color?\n').lower()
while second != 'red' and second != 'yellow' and second != 'blue':
    print('Sorry, {} is not a primary color, try again!'.format(second))
    second = input('Could you give me a second primary color?\n').lower()
print('Awesome!')

color_list = [first, second]
if first == second:
    print(f'{first} plus {second} is {first}')
elif color_list.count('red') == 1 and color_list.count('yellow') == 1:
    print(f'{first} plus {second} is orange')
elif color_list.count('red') == 1 and color_list.count('blue') == 1:
    print(f'{first} plus {second} is purple')
elif color_list.count('yellow') == 1 and color_list.count('blue') == 1:
    print(f'{first} plus {second} is green')
