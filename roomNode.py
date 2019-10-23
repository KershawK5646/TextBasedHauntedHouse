# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:54:53 2019

@author: kyler
"""

class RoomNode(object):
    def __init__(self, data, north = None, south = None, east = None, west = None):
        self.data = data
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __str__ (self):
        return str(self.data)