# -*- coding: utf-8 -*-
"""
The room.py
"""

class Room:
    """The room object"""
    def __init__ (self, roomId, name, description):
        """Create a room object"""
        self.roomId = roomId
        self.name = name
        self.description = description
        
        #self.exits = {} # empty dictionary
        
    def __str__ (self):
        """Create a human readable version"""
        output = "Name: " + self.name
        output += "\n"
        output += "Description: " + self.description
        #output += "Exits: " + str(self.exits)
        return output