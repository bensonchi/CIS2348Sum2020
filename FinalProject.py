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
            inventory_list.append(Inventory(item_ID=row[0], manufacturer=row[1], item_type=row[2], damaged=row[3]))

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


# returns the total number of different item types, but didn't ended up using
'''def count_total_types(inv_list):  
    inventory_list.sort(key=lambda x: x.item_type)  # sort objects by item_type so that same types are together
    count = 1
    type_name = inv_list[0].item_type  # initiate the key for comparison as the first type and initiate count as 1
    for inventory in inv_list:
        if inventory.item_type != type_name:d
            count += 1
            type_name = inventory.item_type
    inventory_list.sort(key=lambda x: x.manufacturer)  # return the objects to original order: by manufacture
    return count'''


def get_item_types(inv_list):  # function that returns a list of all item types (non-repeating)
    types = []
    for i in inv_list:
        types.append(i.item_type)
    types = list(dict.fromkeys(types))  # removes duplicate from the list
    return types


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


def write_damaged_inventory(inv_list):
    inventory_list.sort(key=lambda x: x.price, reverse=True)  # sort the list so that more expensive items appear first
    with open('DamagedInventory.csv', 'w') as di_file:
        for inv in inv_list:
            if inv.damaged == 'damaged':
                di_file.write('{},{},{},{},{}\n'.format(inv.item_ID, inv.manufacturer, inv.item_type, inv.price,
                                                        inv.service_date))


def interactive_query(user_ma, user_it, inv_list):
    found = False
    for inv in inv_list:
        if inv.manufacturer == user_ma and inv.item_type == user_it and inv.service_date<datetime.date.today():
            print('Your item is:{} {} {} {}'.format(inv.item_ID, inv.manufacturer, inv.item_type, inv.price))
            found = True
    if not found:
        print('No such item in inventory')


if __name__ == '__main__':
    inventory_list = read_files()
    write_full_inventory(inventory_list)
    write_type_inventory(inventory_list)
    write_past_service_date_inventory(inventory_list)
    write_damaged_inventory(inventory_list)

    user_manufacturer = input('Please enter manufacturer name:')
    user_item_type = input('Please enter item type:')
    interactive_query(user_manufacturer, user_item_type, inventory_list)