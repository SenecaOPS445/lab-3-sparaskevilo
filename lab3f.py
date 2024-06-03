#!/usr/bin/env python3

my_list = [1, 2, 3, 4, 5]

#Function to add +1 to last item in list
#Convert list data type to integer to perform mathematical operation
def add_item_to_list(ordered_list):
    last_item=int(ordered_list[-1])
    ordered_list.append(last_item + 1)

#Remove all values found in items_to_remove list from ordered list
#Create list copy to prevent issues with editing original list while looping
def remove_items_from_list(ordered_list, items_to_remove):
    for items in ordered_list.copy():
        if items in items_to_remove:
            ordered_list.remove(items)
         

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)