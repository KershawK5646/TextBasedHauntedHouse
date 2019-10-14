# -*- coding: utf-8 -*-
"""
node.py
Node classes for one-way linked structures and two-way
linked structures.
"""

class Node(object):
    def __init__(self, data, next= None):
        """ Instantiates a Node with a defauly next of None"""
        self.data = data
        self.next = next
        
class TwoWayNode(Node):
    def _init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous
        
class FourWayNode(object):
    """Four way node don't have a prev and next
    but instead, a north, south, east, west
    """
    def __init__(self, data, north = None, south = None, east = None, west = None):
        self.data = data
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        
        
