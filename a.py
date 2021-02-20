from collections import namedtuple
# ItemToPurchase = namedtuple('ItemToPurchase', ['item_name', 'item_price', 'item_quantity', 'item_description'])

# ShoppingCart = namedtuple('ShoppingCart', ['customer_name', 'current_date', 'cart_items'])


# def construct_item(name="none", price=0, quantity=0, description="none"):
#     """Create and returns a named tuple."""
#     item = ItemToPurchase(item_name=name, item_price=price, item_quantity=quantity, item_description=description)
#     return item


# def print_item_cost(item_tuple):
#     """Print the item cost."""
#     print('{} {} @ ${} = ${:.0f}'.format(item_tuple.item_name, item_tuple.item_quantity, item_tuple.item_price, item_tuple.item_quantity * item_tuple.item_price))


# def print_item_description(item_tuple):
#     """Print item_name and item_description"""
#     print('{}: {}'.format(item_tuple.item_name, item_tuple.item_description))


# def construct_cart(name='none', date='January 1, 2016', item=[]):
# # Initializes customer_name = "none", current_date = "January 1, 2016", cart_items to an empty list
#     pass


# if __name__ == "__main__":
#     print('Item 1')
#     item1_name = input('Enter the item name:\n')
#     item1_price = int(input('Enter the item price:\n'))
#     item1_quantity = int(input('Enter the item quantity:\n'))
#     item1 = construct_item(item1_name, item1_price, item1_quantity)

#     print('\nItem 2')
#     item2_name = input('Enter the item name:\n')
#     item2_price = int(input('Enter the item price:\n'))
#     item2_quantity = int(input('Enter the item quantity:\n'))
#     item2 = construct_item(item2_name, item2_price, item2_quantity)

#     print('\nTOTAL COST')
#     print_item_cost(item1)
#     print_item_cost(item2)
#     print('\nTotal: ${}'.format(item1_quantity * item1_price + item2_quantity * item2_price))

