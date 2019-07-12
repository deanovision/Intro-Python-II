# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} was added to inventory")

    def remove_from_inventory(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                print(f"{item.name} was removed from inventory")
                return item
            else:
                return None

    def list_inventory(self):
        if self.inventory == []:
            print("no items currently in inventory")
        else:
            inventory = ", ".join([item.name for item in self.inventory])
            # for item in self.inventory:
            #     print(f"items currenlty in inventory: {item.name}")
            print(f"items currenlty in inventory: {inventory}")

    def locate_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
        else:
            return None

    def move_player(self, direction):
        str = f"{direction}_to"
        next_room = getattr(self.current_room, str)
        if next_room:
            self.current_room = next_room
        else:
            print("sorry you can't move there")
