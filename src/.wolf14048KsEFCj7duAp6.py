from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item_list):
        self.name = name
        self.description = description
        self.item
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.list = []

    def add_items_to_room(self, item_list):
        for item in item_list:
            self.list.append(Item(item["name"], item["description"]))
