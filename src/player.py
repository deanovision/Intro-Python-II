# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    # def update_room(self, room):
    #     if room == "Foyer":
    #         self.current_room = "foyer"
    #     elif room == "Outside Cave Entrance":
    #         self.current_room = "outside"
    #     elif room == "Grand Overlook":
    #         self.current_room = "overlook"
    #     elif room == "Narrow Passage":
    #         self.current_room = "narrow"
    #     elif room == "Treasure Chamber":
    #         self.current_room = "treasure"
