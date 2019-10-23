"""
9/27
@author: norrisa
"""

# possibly make the conjugation dictionaries global

def main():
    """ a text parser. the program should ask the user
    for commands in the VERB NOUN format, for example
    eat apple
    get key
    """
    """
    # main loop: continue asking user for input until they
    # enter 'quit'

    # ask user for a command
    # if invalid, ask again
    # invalid means not two words,
    # not a known verb, or not a known noun
    #
    
    # if command is valid, carry it out
    # right now, 'carry it out' just means say
    # that the task was done
    # example:
    # > eat apple
    # Okay, I ate the apple
    #
    """
    """ parsing a command
    parsing a command involves these steps:
    1. split it into verb and noun
    2. look up verb to confirm it is a known verb
    3. look up noun to confirm it is a known noun
    4. execute the command

    executing a command involves these steps:
    1. look up the verb in the conjugation dictionary
    2. find the past tense of the verb
    3. use the past tense to say 'okay, i did the thing'
    """
    verbs = ['go','eat','get','drop']
    nouns = ['north', 'south', 'apple', 'key']
    
    while True:
        # split it into verb and noun
        verb,noun = getCommand()
        print('verb=',verb,'noun=',noun)
        if verb == 'quit':
            print("exiting")
            break
        
        
        if verb not in verbs:
            # look up verb to confirm it is a known verb
            print("I don't know how to '"+verb+"'")
        elif noun not in nouns:
            # look up noun to confirm it is a known noun
            print("I see no",noun,"here")
        else:
            # execute the command
            print("okay")
            
            
            
            
        
    
    
def getCommand():
    """ ask the user for input
    returns a tuple, verb and noun
    """
    commandString = input("> ")
    commandList = commandString.split()
    
    # commands need to have verb and noun
    # unless the command is just 'quit'
    if commandList[0] == "quit":
        return (commandList[0],"")
    if len(commandList) != 2:
        print("Command must be exactly two words")
        return getCommand()
    # command is two words exactly, pack them
    # and return
    return (commandList[0],commandList[1])
    
    
# start the program
main()