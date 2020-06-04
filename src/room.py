# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, *item_list):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.list = []
        if len(item_list) > 0:
            for item in item_list:
                self.list.append(item)

    def add_item(self, item):
        self.list.append(item)

    def remove_item(self, item):
        self.list.remove(item)

    def locate_item(self, item_name):
        for item in self.list:
            if item.name.lower() == item_name.lower():
                return item
            else:
                return None

    def print_items(self):
        if self.list == []:
            print("No items available in this room")
        else:
            for item in self.list:
                print(f"Items available: {item.name}")
                # list_of_items_by_name = []
                # list_of_items_by_name.append(item.name)
                # print(f"Items available: {list_of_items_by_name}")

    def __str__(self):
        return f"{self.name} \n {self.description} \n"
