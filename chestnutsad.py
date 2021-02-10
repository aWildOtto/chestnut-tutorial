num_dict = {'Jersey number': [], 'Rating': []}
jersy = 0
rating = 0

for i in range(0, 5):
    jersey = int(input(f'Enter player {i+1}\'s jersey number:\n'))
    rating = int(input(f'Enter player {i+1}\'s rating:\n'))
    print()
    num_dict['Jersey number'].append(jersey)
    num_dict['Rating'].append(rating)

print('ROSTER')
for i in range(0, 5):
    print('Jersey number: {}, Rating: {}'.format(
        num_dict['Jersey number'][i], num_dict['Rating'][i]))


def print_menu():
    '''
    print the option menu
    '''
    print('''\nMENU
    a - Add player
    d - Remove player
    u - Update player rating
    o - Output roster
    q - Quit\n''')


print_menu()
option = input('Choose an option:\n')

if option == 'a':
    jersey = int(input(f'Enter a new player\'s jersey number:\n'))
    rating = int(input(f'Enter the player\'s rating:\n'))
    print()
    num_dict['Jersey number'].append(jersey)
    num_dict['Rating'].append(rating)
    print_menu()
    option = input('Choose an option:\n')

if option == 'd':
    del_num = int(input('Enter a jersey number:'))
    del_index = num_dict['Jersey number'].index(del_num)
    del num_dict['Jersey number'][del_index]
    del num_dict['Rating'][del_index]
    print_menu()
    option = input('Choose an option:\n')

if option == 'u':
    up_jersey = int(input(f'Enter a jersey number:\n'))
    up_rating = int(input(f'Enter a new rating for player:\n'))
    up_index = num_dict['Jersey number'].index(up_jersey)
    num_dict['Rating'][up_index] = up_rating
    print_menu()
    option = input('Choose an option:\n')

if option == 'o':
    print('ROSTER')
    for i in range(len(num_dict['Jersey number'])):
        print('Jersey number: {}, Rating: {}'.format(
            num_dict['Jersey number'][i], num_dict['Rating'][i]))
    print_menu()
    option = input('Choose an option:\n')

if option == 'q':
    pass
