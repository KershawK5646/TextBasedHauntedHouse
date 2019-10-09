# -*- coding: utf-8 -*-
"""
The room.py
"""

class Room:
    """The room object"""
    def __init__ (self, roommId, name, description):
        """Create a room object"""
        self.roomId = roomId
        self.name = name
        self.description = description
        
    def __str__ (self):
        """Create a human readable version"""
        output = "Name: " + self.name
        output += "\n" + "Description: " + self.description
        return output
    
    
        