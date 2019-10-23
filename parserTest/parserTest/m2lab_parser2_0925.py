# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:03:37 2017

@author: norrisa8373
"""

def main():
    # text parser
    
    commandString = "";
    verbs = ['eat','go','get','drop']
    nouns = ['north', 'south', 'key' ]
    
    # conjugate verbs
    verb_lookup = {
            'eat':'ate',
            'go':'went to',
            'get':'got',
            'drop':'dropped'            
            }
    
    while commandString != "quit":
        commandString = input("> ")
        # exit if command is quit
        if commandString == 'quit':
            print('goodbye')
            break
        command = commandString.split()
        printCommand(command)
        # error if command is not exactly two words
        if len(command) != 2:
            print('Input commands in the format "verb noun"')
            continue
        
        #command list is valid, parse it
        verb = command[0]
        noun = command[1]
        if verb not in verbs:
            print("I don't know the verb '"+verb+"'")
            
        elif noun not in nouns:
            print("I see no",noun,"here")
            
        else:
            print("Okay, I",verb_lookup[verb],"the",noun)
        
    
def printCommand(command): 
    for word in command:
        print (word)
    
    
main()
