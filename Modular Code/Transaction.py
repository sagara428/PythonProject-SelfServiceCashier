# Importing tabulate
from tabulate import tabulate

class Transaction:
    '''A class for transaction purposes.'''

    def __init__(self):
        # Initializing empty shopping cart dictionary 
        self.shopping_cart = {}
    
    def add_item(self):
        '''
        Method to add one or more items to shopping cart
        
        Parameters:
            item_name (str): Name of the item
            quantity (int): Quantity of the item
            price (int): Unit price of the item
            continue_loop (str): looping break/continue indicator
        '''
        #while loop to add items continously if desired
        while True:
            try: #initialize exception handling
                #Input item name, quantity, and price
                self.item_name = input('Input item name: ').capitalize()
                self.quantity = int(input('Input quantity: '))
                self.price = int(input('Input item price: '))

            except ValueError:
                    # Shows Error alert and instruction then continue looping
                    print('Quantity or price must be numeric')
                    print('Please enter valid input')
                    print('-----------------------------------------------')
                    continue
            
            # Shows added item
            print(f'{self.item_name} with quantity {self.quantity} '
                f'and unit price {self.price} is added to shopping cart')
            print('-----------------------------------------------') 
            
            # Update shopping_cart dictionary with added items
            self.shopping_cart.update({self.item_name: [self.quantity, self.price]})
                
            # While loop to store looping break indicator  
            while True:
                #Input looping break indicator
                self.continue_loop = input('Add more? (y/n): ').lower()
                #If the input is correct break the loop
                if self.continue_loop == 'n':
                    break
                elif self.continue_loop == 'y':
                    break
                
                # Shows instruction for wrong input
                print('Please enter "y" or "n"')
                print('-----------------------------------------------')
            
            # Conditional to break looping if the indicator is "n" 
            # or continue the looping if the indicator is "y"
            if self.continue_loop == 'n':
                break
            else:
                continue

    def update_item_name(self):
        '''
        Method to update item name in shopping cart
        
        Parameters:
            item_name (str): Item name which needs to be changed
            new_item_name (str): New name for the item
        '''
        # While loop to let users try again if the input is wrong
        while True:
            # Check if the shopping cart is empty
            if len(self.shopping_cart) == 0:
                # Shows alert and instruction
                print('The shopping cart is empty!')
                print('Please add some items')
                break 

            # Input item name
            self.item_name = input('Item name: ').capitalize()
            # Indicator to check whether the item name is in 
            # shopping cart or not
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Conditional to change item name then break the loop
            # if the indicator is True
            if is_in_cart == True:
                # Input new item name
                self.new_item_name = input('New item name: ').capitalize()
                self.shopping_cart[self.new_item_name] = self.shopping_cart[self.item_name]
                del self.shopping_cart[self.item_name]

                # Shows success message
                print('item name updated successfully')
                print('-----------------------------------------------')
                break
            
            # Shows alert and instruction if the input is wrong
            print('There is no such item in shopping cart!')
            print('Please try again')
            print('-----------------------------------------------')

    def update_item_quantity(self):
        '''
        Method to update the quantity of an item in shopping cart
        
        Parameters:
            item_name (str): Item name which quantity needs to be changed
            new_quantity (str): New quantity of the item
        '''
        # While loop to let users try again if the input is wrong
        while True:
            # Check if the shopping cart is empty
            if len(self.shopping_cart) == 0:
                # Shows alert and instruction
                print('The shopping cart is empty!')
                print('Please add some items')
                break 

            # Input item name
            self.item_name = input('Item name: ').capitalize()
            # Indicator to check whether the item name is in 
            # shopping cart or not
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Conditional to change item quantity then break the loop
            # if the indicator is True
            if is_in_cart == True:
                # Input new item quantity
                self.new_quantity = int(input('New item quantity: '))
                self.shopping_cart[self.item_name][0] = self.new_quantity

                # Shows success message
                print('item quantity updated successfully')
                print('-----------------------------------------------')
                break
            
            # Shows alert and instruction if the input is wrong
            print('There is no such item in shopping cart!')
            print('Please try again')
            print('-----------------------------------------------')

    def update_item_price(self):
        '''
        Method to update the price of an item in shopping cart
        
        Parameters:
            item_name (str): Item name which quantity needs to be changed
            new_price (int): New price of the item
        '''
        # While loop to let users try again if the input is wrong
        while True:
            # Check if the shopping cart is empty
            if len(self.shopping_cart) == 0:
                # Shows alert and instruction
                print('The shopping cart is empty!')
                print('Please add some items')
                break 

            # Input item name
            self.item_name = input('Item name: ').capitalize()
            # Indicator to check whether the item name is in 
            # shopping cart or not
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Conditional to change item price then break the loop
            # if the indicator is True
            if is_in_cart == True:
                self.new_price = int(input('New item price: '))
                self.shopping_cart[self.item_name][1] = self.new_price

                # Shows success message
                print('item price updated successfully')
                print('-----------------------------------------------')
                break

            # Shows alert and instruction if the input is wrong
            print('There is no such item in shopping cart!')
            print('Please try again')
            print('-----------------------------------------------')

    def delete_item(self):
        '''
        Method to remove an item from shopping cart
        
        Parameters:
            item_name (str): Item name which wants to be removed
        '''
        # While loop to let users try again if the input is wrong
        while True:
            # Check if the shopping cart is empty
            if len(self.shopping_cart) == 0:
                # Shows alert and instruction
                print('The shopping cart is empty!')
                print('Please add some items')
                break 
            
            # Input item name
            self.item_name = input('Item name: ').capitalize()
            # Indicator to check whether the item name is in 
            # shopping cart or not
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Conditional to remove the item from shopping cart
            # if the indicator is True then break the loop
            if is_in_cart == True:
                self.shopping_cart.pop(self.item_name)

                # Shows success message
                print('item deleted successfully')
                print('-----------------------------------------------')
                break
            
            # Shows alert and instruction if the input is wrong
            print('There is no such item in shopping cart!')
            print('Please try again')
            print('-----------------------------------------------')

    def reset_transaction(self):
        '''Method to delete all items from shopping cart'''
        # Clear all keys and values in shopping_cart dictionary
        self.shopping_cart.clear()

        # Shows success message
        print('Shopping cart is now empty!')
        print('-----------------------------------------------')
    
    def check_order(self):
        '''Method to check and show the items in shopping cart'''
        # Data for shopping list table
        self.data = [
            ['Item Name', 'Quantity', 'Price', 'Total Price'] # Headers
        ]

        # For loop to add data for each headers
        for key, value in self.shopping_cart.items():
            self.data.append([key, value[0], value[1], value[0]*value[1]])
        
        # Print table of item lists in shopping cart
        print(tabulate(self.data, headers="firstrow"))

        # For loop to check the quantity and price 
        # of items in shopping list
        for key, value in self.shopping_cart.items():
            if value[0] < 0 or value[1] < 0:
                # Shows alert and instruction for wrong input
                print(f'The quantity or price of {key} is wrong')
                print('Please update the item quantity or price') 
    
    
    def total_price(self):
        '''Function to calculate total price'''
        # Initialize total_price variable as 0
        total_price = 0

        # Calculate the sum of each item's total price
        for index in range(1, len(self.data)):
            total_price += self.data[index][3]

        # Conditional for discount     
        if total_price > 500_000:
            discount = 0.1 # 10% discount
            total_price -= discount * total_price
            print('You get 10% discount!')
        elif total_price > 300_000: 
            discount = 0.08 # 8% discount
            total_price -= discount * total_price
            print('you get 8% discount!')
        elif total_price > 200_000:
            discount = 0.05 #5% discount
            total_price -= discount * total_price
            print('you get 5% discount!')
        else:
            # Shows discount list if the user
            # does not get any discount
            print('You get no discount')
            print('''
            Discount list if you are interested:
            5%: if total price is greater than 200000
            8%: if total price is greater than 300000
            10%: if total price is greater than 500000
            ''')

        # Shows the total price after discount (if any)
        print(f'Total price: Rp.{total_price:,.2f}')