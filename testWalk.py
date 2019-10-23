# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:29:33 2019

@author: kyler
"""
from house import House

# Test Walk
def main():
    # Create house
    hauntedHouse = House()
    
    # Start player in Master Bedroom
    me = hauntedHouse.start
    print(me)
    print("\n")
    print(me)
    print("\n")
    
    # Travel south to master Bath
    print("Move South")
    me = me.south
    print(me)
    print("\n")
    
    # Travel North to Master bedroom
    print("Move North")
    me = me.north
    print(me)
    print("\n")
    
    # Travel East to livingroom
    print("Move East")
    me = me.east
    print(me)
    print("\n")
    
    # Travel north to porch
    print("Move North")
    me = me.north
    print(me)
    print("\n")
    
    # Travel south to livingroom
    print("Move South")
    me = me.south
    print(me)
    print("\n")
    
    # Travel East to Kitchen
    print("Move East")
    me = me.east
    print(me)
    print("\n")
    
    # Travel south to Diningroom
    print("Move South")
    me = me.south
    print(me)
    print("\n")
    
    # Travel West to Stairs
    print("Move west")
    me = me.west
    print(me)
    print("\n")
    
    # Travel north to Gameroom
    print("Move North")
    me = me.north
    print(me)
    print("\n")
    
    # Travel East to Guest Bedroom
    print("Move East")
    me = me.east
    print(me)
    print("\n")
    
    # Travel south to Guest Bathroom
    print("Move South")
    me = me.south
    print(me)
    print("\n")
    
main()