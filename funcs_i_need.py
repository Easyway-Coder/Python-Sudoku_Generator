import random


def take_items_from_list(list: list, addition=""):
    items_concatenated = ""
    for item in list:
        items_concatenated += str(item)
        items_concatenated += addition
    return items_concatenated


def shuffle_list(list: list):
    length = len(list)
    for item in list:
        pop_item = list.pop(list.index(item))
        list.insert(random.randint(0, length-1), pop_item)
    return list
    

