from collections import namedtuple

Customer = namedtuple('Customer', 'name order')

Store = namedtuple('Store', 'name inventory')


def part1(customers, stores):
    """
    Function that does

    Part 1:
        Part 1A: Assuming the list is sorted in decending price, calculate and print
        the average item price at each store in ascending price order (reverse the list).
        Part 1B: If the list is out of order, print an error message.
    """
    store_list = []
    for store in stores:
        store_items = store.inventory.keys()
        allItemtotal = 0
        allItemquantity = 0
        for item in store_items:
            price = store.inventory[item][0]
            quantity = store.inventory[item][1]
            total_price = price * quantity
            allItemtotal += total_price
            allItemquantity += quantity
        avg_price = allItemtotal / allItemquantity

        store_list.append({
            'avg_price': avg_price,
            'name': store.name,
            'inventory': store.inventory
        })
    store_list.reverse()
    prev = None
    for store in store_list:
        print('The average item at {} costs ${:.2f}'.format(
            store['name'], store['avg_price']))
        if(prev != None):
            if prev >= store['avg_price']:
                print('Error: Outdated information, quitting program...')
                exit(1)

        prev = store['avg_price']
    return store_list


def part2(customers, stores):
    """asdklfjlka

      Part 2: print sorted customer order
          Jared wants 2 Chips, 100 Crisps.
          Shannon does not want anything.
    """
    customer_orders = []
    for customer in customers:
        customer_items = customer.order.keys()

        customer_order_list = []
        for item in customer_items:
            customer_order_list.append({
                'orderName': item,
                'orderCount': customer.order[item]
            })
        customer_order_list = sorted(customer_order_list, key=sortFunc)

        customer_orders.append({
            'name': customer.name,
            'order_list': customer_order_list
        })
    return customer_orders


def drone_delivery_service(customers, stores):
    """
    Print Instructions for Drone Delivery Service.

    :param customers: [Customer(str, {str: float})]
    :param stores: [Store(str, {str: [float, int]})]
    """
    customer_totals = {}  # Use this for part 4

    store_list = part1(customers, stores)

    customer_orders = part2(customers, stores)

    # print('customer_orders->', customer_orders)
    # Part 3 & 4 might involve code from part 2...
    # Part 3
    # print(store_items)
    # customer_bought_count = {}  # Use this for part 4

    for cust_order in customer_orders:
        print('cust_order __', cust_order)
        if not cust_order['order_list']:
            print('{} does not want anything.'.format(cust_order['name']))
            pass
        else:
            customer_totals[cust_order['name']] = {}
            print('{} wants'.format(cust_order['name']), end=' ')
        # print the line XXX wants x chips, x crips, x Ruby.
        for order in cust_order['order_list']:
            print('order====', order)
            print('{} {}'.format(order['orderCount'],
                                 order['orderName']), end='')
            if order == cust_order['order_list'][-1]:
                print('.')
            else:
                print(',', end=' ')
        # print('customer_totals--->', customer_totals)
        # print the lines XXX Purchased x chips, x crips, x Ruby from xxx
        for order in cust_order['order_list']:
            # print(order)

            for store in store_list:
                # print(customer_totals[cust_order['name']][store['name']])
                # store => {'avg_price': 1.0, 'name': '99-Cent Store'}
                # store(name='Albertsons', inventory={'Chips': [5.00, 10], 'Pizza': [12.00, 3], 'Fries': [5.00, 1]})
                if store['name'] not in customer_totals[cust_order['name']].keys():
                    customer_totals[cust_order['name']][store['name']] = 0
                # print(customer_totals)
                if order['orderName'] in store['inventory']  \
                        and store['inventory'][order['orderName']][1] > 0  \
                        and order['orderCount'] > 0:
                    # print("store['inventory'][order['orderName']][1] --->", store['inventory'][order['orderName']][1])
                    buyCount = min(
                        order['orderCount'], store['inventory'][order['orderName']][1])
                    print('\tPurchased {} {} at {} for ${:.2f}'.format(
                        buyCount, order['orderName'], store['name'], buyCount * store['inventory'][order['orderName']][0]))

                    customer_totals[cust_order['name']][store['name']
                                                        ] += buyCount * store['inventory'][order['orderName']][0]
                    # customer_bought_count[cust_order['name']][store['name']]=buyCount
                    order['orderCount'] -= buyCount
                    store['inventory'][order['orderName']][1] -= buyCount
                # print(customer_totals[cust_order['name']][store['name']])
                # print('\t\tcustomer_totals--->',customer_totals)

            if order['orderCount'] > 0:
                print('\tAll stores were sold out of {}; {} could not purchase {} {}'.format(
                    order['orderName'], cust_order['name'], order['orderCount'], order['orderName']))

    # ----End here----
    # print(customer_totals)
    # print('\n')
    # print( stores)
    return customer_totals, stores


def sortFunc(item):
    return item['orderName']


if __name__ == '__main__':
    # Set submit_mode to False to be able to run this code in python tutor or development mode
    # Ensure it is set to True when submitting code
    submit_mode = False
    if submit_mode:
        drone_delivery_service(*eval(input()))
    else:
        print("THIS IS A TEST RUN - IF YOU ARE SEEING "
              "THIS IN SUBMIT MODE, SET submit_mode = True AND RERUN")
        drone_delivery_service(
            [Customer(name='Jared', order={'Chips': 2, 'Crisps': 100}),
             Customer(name='Shannon', order={}),
             Customer(name='Caio', order={'Fries': 1, 'Chips': 10})],
            [Store(name='Vons', inventory={'Cereal': [10.00, 10]}),
             Store(name='Trader Joes', inventory={'Chips': [9, 1]}),
             Store(name='Albertsons', inventory={
                   'Chips': [5.00, 10], 'Pizza': [12.00, 3], 'Fries': [5.00, 1]}),
             Store(name='99-Cent Store', inventory={'Salsa': [1.00, 1]})])
