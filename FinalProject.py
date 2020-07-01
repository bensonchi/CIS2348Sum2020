# Name:Baichuan Chi
# PSID:1938207
import csv
import datetime


class Inventory:
    def __init__(self, item_ID=' ', manufacturer=' ', item_type=' ', price=-1, service_date=' ', damaged=' '):
        self.item_ID = item_ID
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged


def read_files():  # read all the csv files and return a list of inventory objects sorted by manufacturer name
    inventory_list = []  # initiate a list to contain Inventory objects
    with open('ManufacturerList.csv', 'r') as ml_file:
        item_reader = csv.reader(ml_file, delimiter=',')
        for row in item_reader:  # fill the list of Inventory object
            inventory_list.append(Inventory(item_ID=row[0].strip(), manufacturer=row[1].strip(),
                                            item_type=row[2].strip(), damaged=row[3].strip()))

    pl_dict = {}  # initiate a dictionary to pair item id with price
    with open('PriceList.csv', 'r') as pl_file:
        price_reader = csv.reader(pl_file, delimiter=',')
        for row in price_reader:
            pl_dict[row[0]] = row[1]

    sdl_dict = {}  # initiate a dictionary to pair item id with service date
    with open('ServiceDatesList.csv', 'r') as sdl_file:
        service_date_reader = csv.reader(sdl_file, delimiter=',')
        for row in service_date_reader:
            sdl_dict[row[0]] = row[1]

    for inventory in inventory_list:  # fill the price and service date field in the class
        inventory.price = pl_dict[inventory.item_ID]
        inventory.service_date = sdl_dict[inventory.item_ID]
    inventory_list.sort(key=lambda x: x.manufacturer)

    return inventory_list


def write_full_inventory(inv_list):  # function to write FullIntentory csv file.
    with open('FullInventory.csv', 'w') as fi_file:
        for inventory in inv_list:
            fi_file.write('{},{},{},{},{},{}\n'.format(inventory.item_ID, inventory.manufacturer, inventory.item_type,
                                                       inventory.price, inventory.service_date, inventory.damaged))


def get_item_types(inv_list):  # function that returns a list of all item types (non-repeating)
    types = []
    for i in inv_list:
        types.append(i.item_type)
    types = list(dict.fromkeys(types))  # removes duplicate from the list
    return types


def get_item_manufacturer(inv_list):  # function that returns a list of all manufacturer (non-repeating)
    manufacturer = []
    for i in inv_list:
        manufacturer.append(i.manufacturer)
    manufacturer = list(dict.fromkeys(manufacturer))  # removes duplicate from the list
    return manufacturer


def write_type_inventory(inv_list):  # function to write csv files of different types' inventory.
    types = get_item_types(inv_list)
    for ty in types:  # iterate through all tha item types
        with open(ty+'Inventory.csv', 'w') as ti_file:  # item type name will be included in the file name
            for inv in inv_list:
                if inv.item_type == ty:  # write only the same type in one file
                    ti_file.write('{},{},{},{},{}\n'.format(inv.item_ID, inv.manufacturer, inv.price, inv.service_date,
                                                            inv.damaged))


def write_past_service_date_inventory(inv_list):  # function to write PastServiceDateInventory.csv file
    today = datetime.date.today()
    with open('PastServiceDateInventory.csv', 'w') as psdi_file:
        for inv in inv_list:
            my_list = inv.service_date.split('/')  # convert string to date data type so we can compare with 'today'
            inv_date = datetime.date(int(my_list[2]), int(my_list[0]), int(my_list[1]))
            if today > inv_date:
                psdi_file.write('{},{},{},{},{}\n'.format(inv.item_ID, inv.manufacturer, inv.item_type, inv.price,
                                                          inv.service_date, inv.damaged))


def write_damaged_inventory(inv_list):  # function for write DamagedInventory.csv file
    inv_list.sort(key=lambda x: x.price, reverse=True)  # sort the list so that more expensive items appear first
    with open('DamagedInventory.csv', 'w') as di_file:
        for inv in inv_list:
            if inv.damaged == 'damaged':
                di_file.write('{},{},{},{},{}\n'.format(inv.item_ID, inv.manufacturer, inv.item_type, inv.price,
                                                        inv.service_date))


def find_max_price(inv_list):
    # function to find the most expensive item in the list
    maximum = -1
    max_object = Inventory()
    for inv in inv_list:
        if int(inv.price) > maximum:
            maximum = int(inv.price)
            max_object = inv
    return max_object


def find_user_item(user_input, inv_list):
    type_list = get_item_types(inv_list)
    manufacturer_list = get_item_manufacturer(inv_list)
    user_str = user_input.split(' ')

    type_counter = 0  # a counter to track how many types appeared in the user string
    manufacturer_counter = 0  # a counter to track how many manufacturer appeared in the user string
    user_type = ''  # used to record the user desired item_type
    user_manufacturer = ''  # used to record the user desired manufacturer
    manufacturer_available_in_type = False  # indicate whether certain manufacturer has a certain item type
    user_object_list = []  # used to contain item objects that fits the criteria entered by user
    user_type_list = []  # a list of objects that of the user selected type
    today = datetime.date.today()
    for inv in inv_list:  # remove items that past service date as they will not be considered for output
        my_list = inv.service_date.split('/')  # convert string to date data type so we can compare with 'today'
        inv_date = datetime.date(int(my_list[2]), int(my_list[0]), int(my_list[1]))
        if today > inv_date:
            inv_list.remove(inv)
    for inv in inv_list:  # remove items that are damaged as they will not be considered for output
        if inv.damaged == 'damaged':
            inv_list.remove(inv)

    for s in user_str:  # iterate through the user string and compare each term with types and manufacturers
        for types in type_list:
            if s == types:
                type_counter += 1
                user_type = types  # record the types entered by the user
        for manufacturer in manufacturer_list:
            if s == manufacturer:
                manufacturer_counter += 1
                user_manufacturer = manufacturer  # record the manufacturer entered by the user

    for inv in inv_list:  # generate a list of objects that fit both manufacturer and item type
        if inv.manufacturer == user_manufacturer and inv.item_type == user_type:
            user_object_list.append(inv)
            manufacturer_available_in_type = True

    if type_counter == 1 and manufacturer_counter == 1 and manufacturer_available_in_type:
        # a correct input should contain 1 type and 1 manufacturer and the manufacturer should be available for type
        best_object = find_max_price(user_object_list)
        print('Your item is:{} {} {} {}'.format(best_object.item_ID, best_object.manufacturer, best_object.item_type,
                                                best_object.price))
        also_consider(best_object.item_type, inv_list, int(best_object.price))

    elif type_counter == 1:  # if correct type is entered once, output the most expensive item in that type
        for inv in inv_list:  # generate a list of objects that of the type that use chosen
            if inv.item_type == user_type:
                user_type_list.append(inv)
        best_object = find_max_price(user_type_list)
        print('Your item is:{} {} {} {}'.format(best_object.item_ID, best_object.manufacturer, best_object.item_type,
                                                best_object.price))
        also_consider(user_type, inv_list)

    else:
        print('No such item in inventory')


def also_consider(user_type, inv_list, price=-1):  # function to output 'you should also consider' portion
    type_list = []
    object_to_consider = Inventory()  # this is used to contain the recommend item object
    for inv in inv_list:  # fill type_list with only items that fits the item type specified
        if inv.item_type == user_type:
            type_list.append(inv)
    if price == -1:  # this means that no price is not passed to the function, so output the most expensive item in type
        object_to_consider = find_max_price(type_list)
        print('You may, also, consider: {} {} {} {}'.format(object_to_consider.item_ID,
                                                            object_to_consider.manufacturer,
                                                            object_to_consider.item_type, object_to_consider.price))
    else:
        type_list.sort(key=lambda x: x.price, reverse=True)  # sort the list depending on price
        index = 0
        for types in type_list:
            if types.price == price:
                index = type_list.index(types)
        object_to_consider = type_list[index-1]  # recommend a closely priced item of same type
        print('You may, also, consider: {} {} {} {}'.format(object_to_consider.item_ID,
                                                            object_to_consider.manufacturer,
                                                            object_to_consider.item_type, object_to_consider.price))


if __name__ == '__main__':
    inventory_list = read_files()
    write_full_inventory(inventory_list)
    write_type_inventory(inventory_list)
    write_past_service_date_inventory(inventory_list)
    write_damaged_inventory(inventory_list)
    print('\n**************************************************')
    print('**  Welcome to my Inventory Management System!  **')
    print('**************************************************\n')
    user_entry = input('Please enter a item type and manufacturer that you would like to look for ')
    while user_entry != 'q':
        find_user_item(user_entry, inventory_list)
        user_entry = input('\nPlease enter a item type and manufacturer that you would like to look for ')
    print('\n Thank you and good bye!')