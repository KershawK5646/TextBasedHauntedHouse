# -*- coding: utf-8 -*-
"""
House File
"""
from room import Room
from roomNode import RoomNode

class House:
    """ a House contains multiple Room Objects """
    def __init__(self):
        # Create rooms
        void = Room(0, "The Void","You should have never seen this room...")
        masterBedroom = Room(1, "Master Bedroom","A king size bed lays on the far wall. ")
        masterBathroom = Room(2, "Master Bathroom","Mold everywhere...")
        livingroom = Room(3, "Livingroom","Everything is caked in dust.")
        kitchen = Room(4, "Kitchen","There is rotting food and dirty dished piled high.")
        diningroom = Room(5, "Diningroom", "An old table and broken chairs sit in the middle of the room...")
        stairs = Room(6, "Stairs", "A busted old staircase...The carpet is stained in the middle.")
        gameroom = Room(7, "Gameroom", "There's a torn up pool table off to the left and a large TV on the right.")
        guestBedroom = Room (8, "Guest Bedroom", "An old 4 post bedset sits empty in the middle of the wall in front of you")
        guestBathroom = Room (9, "Guest Bathroom","Mold growing everywhere...")
        porch = Room(10, "Front Porch","Rotting boards and the smell of fresh air...You're free.")
        
        self.rooms = [void, masterBedroom, masterBathroom, livingroom, kitchen,
                      diningroom, stairs, gameroom, guestBedroom, guestBathroom,
                      porch]

        # Create Nodes
        #kitchenNode = roomNode("Kitchen")
        voidNode            = RoomNode(void)
        masterBedroomNode   = RoomNode(masterBedroom)
        masterBathroomNode  = RoomNode(masterBathroom)
        livingroomNode      = RoomNode(livingroom)
        kitchenNode         = RoomNode(kitchen)
        diningroomNode      = RoomNode(diningroom)
        stairsNode          = RoomNode(stairs)
        gameroomNode        = RoomNode(gameroom)
        guestBedroomNode    = RoomNode(guestBedroom)
        guestBathroomNode   = RoomNode(guestBathroom)
        porchNode           = RoomNode(porch)
        
        # Link the nodes
        # kitchenNode.east = denNode
        
        # Master Bedroom
        masterBedroomNode.south = masterBathroomNode
        masterBedroomNode.east = livingroomNode
        # Master Bathroom
        masterBathroomNode.north = masterBedroomNode
        # Livingroom
        livingroomNode.north = porchNode
        livingroomNode.east = kitchenNode
        livingroomNode.west = masterBedroom
        # Porch
        porchNode.south = livingroomNode
        # Kitchen
        kitchenNode.south = diningroomNode
        kitchenNode.west = livingroomNode
        # Diningroom
        diningroomNode.north = kitchenNode
        diningroomNode.west = stairsNode
        # Stairs
        stairsNode.east = diningroomNode
        stairsNode.north = gameroomNode
        # Gameroom
        gameroomNode.east = guestBedroomNode
        gameroomNode.south = stairsNode
        # Guest Bedroom
        guestBedroomNode.south = guestBathroomNode
        guestBedroomNode.west = gameroomNode
        # Guest Bathroom
        guestBathroomNode.north = guestBedroomNode
        
        # Create starting point
        self.start = masterBedroomNode
        

