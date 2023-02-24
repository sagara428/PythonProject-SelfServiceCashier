# Importing all methods from Transaction
from Transaction import *

trnsct = Transaction() # Create an object of Transaction class

# Main menu of Self Service Cashier
print('''
-----------------------------------------------
       WELCOME TO SELF SERVICE CASHIER!!!          
-----------------------------------------------
''')
while True:
    print('''
    Choose one of the following features:
    1: Add item.
    2: Check order/shopping cart.
    3: Delete item from shopping cart.
    4: Reset transaction (delete all items).
    5: Update item name.
    6: Update item quantity.
    7: Update item price.
    8: Calculate total price.
    9: Close program.
    ''')
    number = int(input('Input feature\'s number: '))
    if number == 1:
        trnsct.add_item()
    elif number == 2:
        trnsct.check_order()
        print('-----------------------------------------------')
    elif number == 3:
        trnsct.delete_item()
        print('-----------------------------------------------')
    elif number == 4:
        trnsct.reset_transaction()
        print('-----------------------------------------------')
    elif number == 5:
        trnsct.update_item_name()
        print('-----------------------------------------------')
    elif number == 6:
        trnsct.update_item_quantity()
        print('-----------------------------------------------')
    elif number == 7:
        trnsct.update_item_price()
        print('-----------------------------------------------')
    elif number == 8:
        trnsct.total_price()
        print('-----------------------------------------------')
    elif number == 9:
        print('''
        -----------------------------------------------
           Thank you for using self service cashier!
        -----------------------------------------------
        ''')
        break