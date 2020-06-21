# Name:Baichuan Chi
# PSID:1938207


class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):  # Constructor
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):  # print function definition
        total_price = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total_price))


if __name__ == '__main__':
    print('Item 1')  # Prompt user to input information for item 1.
    print('Enter the item name:')
    name1 = input()
    print('Enter the item price:')
    price1 = int(input())
    print('Enter the item quantity:')
    quantity1 = int(input())

    print('\nItem 2')  # Prompt user to input information for item 1.
    print('Enter the item name:')
    name2 = input()
    print('Enter the item price:')
    price2 = int(input())
    print('Enter the item quantity:')
    quantity2 = int(input())

    item1 = ItemToPurchase(name1, price1, quantity1)  # Create two objects of class ItemToPurchase
    item2 = ItemToPurchase(name2, price2, quantity2)
    print()  # blank line for format
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print('\nTotal: ${}'.format(quantity1 * price1 + quantity2 * price2))
