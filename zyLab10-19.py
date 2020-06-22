# Name:Baichuan Chi
# PSID:1938207


class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none'):  # Constructor
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):  # print function definition
        total_price = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total_price))

    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, name_to_remove=''):
        found = False
        for i in self.cart_items:
            if name_to_remove == i.item_name:
                self.cart_items.remove(i)
                found = True
        if not found:
            print('Item not found in cart. Nothing removed.\n')


    def modify_item(self, ItemToPurchase):
        found = False
        print('Enter the new quantity:')
        new_quantity = int(input())
        for i in self.cart_items:
            if i.item_name == ItemToPurchase.item_name:
                found = True
                i.item_quantity = new_quantity
        if not found:
            print('Item not found in cart. Nothing modified.\n')

    def get_num_items_in_cart(self):
        num_items = 0
        for i in self.cart_items:
            num_items += i.item_quantity
        return num_items

    def get_cost_of_cart(self):
        cart_cost = 0
        for i in self.cart_items:
            cart_cost += (i.item_price * i.item_quantity)
        return cart_cost

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print('Number of Items: {}'.format(self.get_num_items_in_cart()))
        print()
        total = 0
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            for i in self.cart_items:
                item_total = i.item_quantity * i.item_price
                print('{} {} @ ${} = ${}'.format(i.item_name, i.item_quantity, i.item_price, item_total))
                total += item_total
        print()
        print('Total: ${}\n'.format(total))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print()
        print('Item Descriptions')
        for i in self.cart_items:
            i.print_item_description()
        print()

    def menu(self):
        print(
            'MENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            "i - Output items' descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n'
        )

    def print_menu(self):
        self.menu()
        choice = input('Choose an option:\n')
        while choice != 'q':
            if choice == 'a':
                print('ADD ITEM TO CART')
                print('Enter the item name:')
                item_name = input()
                print('Enter the item description:')
                item_description = input()
                print('Enter the item price:')
                item_price = int(input())
                print('Enter the item quantity:\n')
                item_quantity = int(input())
                new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                self.add_item(new_item)

            elif choice == 'r':
                print('REMOVE ITEM FROM CART')
                print('Enter name of item to remove:\n')
                remove_item = input()
                self.remove_item(remove_item)

            elif choice == 'c':
                print('CHANGE ITEM QUANTITY')
                print('Enter the item name:')
                name_to_change = input()
                item = ItemToPurchase(name_to_change)
                self.modify_item(item)

            elif choice == 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                self.print_descriptions()

            elif choice == 'o':
                print('OUTPUT SHOPPING CART')
                self.print_total()

            else:
                choice = input('Choose an option:\n')
                continue

            self.menu()
            choice = input('Choose an option:\n')


if __name__ == '__main__':
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print('Customer name: {}'.format(name))
    print("Today's date: {}\n".format(date))
    new_cart = ShoppingCart(name, date)

    new_cart.print_menu()
