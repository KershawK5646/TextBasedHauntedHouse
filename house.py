# -*- coding: utf-8 -*-
"""
House File
"""
from room import Room

class House:
    """ a House contains multiple Room Objects """
    def __init__(self):
        # Create rooms
        start = Room(0, "The Void","You should have never seen this room...")
        kitchen = Room(1, "Kitchen","There is rotting food and dirty dished piled high.")
        bedroom = Room(2, "Bedroom","A king size bed lays on the far wall. ")
        livingroom = Room(3, "Livingroom","Everything is caked in dust.")
        bathroom = Room(4, "Bathroom","Mold everywhere...")
        garage = Room(5, "Garage","There are oil stains splattered on the concrete...")
        
        self.rooms = [start, kitchen, bedroom, livingroom, bathroom, garage]
        
def main():
    house = House()
    for room in house.rooms:
        print(room)

if __name__ == "__main__":
    main()