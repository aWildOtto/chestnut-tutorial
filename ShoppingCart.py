from collections import namedtuple

ItemToPurchase = namedtuple('ItemToPurchase', ['item_name', 'item_price', 'item_quantity', 'item_description'])

ShoppingCart = namedtuple('ShoppingCart', ['customer_name', 'current_date', 'cart_items'])


def construct_item(name="none", price=0, quantity=0, description="none"):
    """Create a named tuple for items customer will purchase."""
    item = ItemToPurchase(item_name=name, item_price=price, item_quantity=quantity, item_description=description)
    return item


def print_item_cost(item_tuple):
    """Print the item cost."""
    print('{} {} @ ${} = ${:.0f}'.format(item_tuple.item_name, item_tuple.item_quantity, item_tuple.item_price, item_tuple.item_quantity * item_tuple.item_price))


def construct_cart(name='none', currentDate='January 1, 2016', item=[]):
    """Create a named tuple for shoppingcart."""
    Cart = ShoppingCart(customer_name=name, current_date=currentDate, cart_items=item)
    return Cart


def add_item(cart_tuple, item_tuple):
    """Create a named tuple for items customer will purchase."""
    cart_tuple[2].append(item_tuple)


def remove_item(cart_tuple, removeName):
    """Create a named tuple for items customer will purchase."""
    for item in cart_tuple[2]:
        if removeName not in item[0] and item == cart_tuple[2][-1]:
            print('Item not found in cart. Nothing removed.')
        elif removeName in item[0]:
            cart_tuple[2].remove(item)
        else:
            pass


def modify_item(cart_tuple, item_tuple):
    """Create a named tuple for items customer will purchase."""
    for item in cart_tuple[2]:
        if item_tuple[0] not in item[0] and item == cart_tuple[2][-1]:
            print('Item not found in cart. Nothing modified.')
        elif item_tuple[0] in item[0]:
            item[2] = item_tuple[2]
        else:
            pass


def get_num_items_in_cart(cart_tuple):
    """Create a named tuple for items customer will purchase."""
    numItem = 0
    for item in cart_tuple[2]:
        numItem += item[2]
    return numItem


def get_cost_of_cart(cart_tuple):
    """Create a named tuple for items customer will purchase."""
    totalCost = 0
    for item in cart_tuple[2]:
        totalCost += item[1] * item[2]
    return totalCost


def print_total(cart_tuple):
    """Create a named tuple for items customer will purchase."""
    if cart_tuple[2] == []:
        print('SHOPPING CART IS EMPTY')
    else:
        for item in cart_tuple[2]:
            # name = item[0]
            # price = item[1]
            # quantity = item[2]
            print('{} {} @ ${} = ${}'.format(item[0], item[2], item[1], item[1] * item[2]))


def print_descriptions(cart_tuple):
    """Create a named tuple for items customer will purchase."""
    for item in cart_tuple[2]:
        def print_item_description(item_tuple):
            """Print item_name and item_description."""
            print('{}: {}'.format(item_tuple.item_name, item_tuple.item_description))
        print_item_description(item)


def print_menu():
    """Create a named tuple for items customer will purchase."""
    print('''MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit\n''')

    option = input('Choose an option:\n')
    return option


if __name__ == "__main__":
    customerName = input('Enter customer\'s name:\n')
    todayDate = input('Enter today\'s date:\n')
    if customerName != '' and todayDate != '':
        customerCart = construct_cart(customerName, todayDate)
    elif customerName != '' and todayDate == '':
        customerCart = construct_cart(name=customerName)
    elif customerName == '' and todayDate != '':
        customerCart = construct_cart(currentDate=todayDate)
    else:
        customerCart = construct_cart()

    print(f'\nCustomer name: {customerCart[0]}')
    print(f'Today\'s date: {customerCart[1]}\n')

    answer = print_menu()
    answerList = ['a', 'r', 'c', 'i', 'o']
    while answer != 'q':
        if answer not in answerList:
            answer = input('Choose an option:\n')
        else:
            if answer == 'a':
                # Add item to cart
                print('ADD ITEM TO CART')
                item_name = input('Enter the item name:\n')
                item_description = input('Enter the item description:\n')
                item_price = int(input('Enter the item price:\n'))
                item_quantity = int(input('Enter the item quantity:\n'))
                itemA = construct_item(item_name, item_price, item_quantity, item_description)
                add_item(customerCart, itemA)
            if answer == 'r':
                # Remove item from cart
                print('REMOVE ITEM FROM CART')
                itemToRemove = input('Enter name of item to remove:\n')
                remove_item(customerCart, itemToRemove)
            if answer == 'c':
                # Change item quantity
                print('CHANGE ITEM QUANTITY')
                ModifyName = input('Enter the item name:\n')
                ModifyQuantity = input('Enter the new quantity:\n')
                newItem = construct_item(name=ModifyName, quantity=ModifyQuantity)
                modify_item(customerCart, newItem)
            if answer == 'i':
                # Output items' descriptions
                print('OUTPUT ITEMS\' DESCRIPTIONS')
                print(f'{customerCart[0]}\'s Shopping Cart - {customerCart[1]}\n')
                print('Item Descriptions')
                print_descriptions(customerCart)
            if answer == 'o':
                # Output shopping cart
                print('OUTPUT SHOPPING CART')
                print(f'{customerCart[0]}\'s Shopping Cart - {customerCart[1]}')
                print(f'Number of Items: {get_num_items_in_cart(customerCart)}\n')
                print_total(customerCart)
                print('\nTotal: ${}'.format(get_cost_of_cart(customerCart)))
            
            print()
            answer = print_menu()
