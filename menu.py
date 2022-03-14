from numpy import *
""" 
======================================================================
                             MENU 1
======================================================================
"""

# Menu options as a dictionary
menu1_options = {
    1: 'S',
    2: 'N',
    3: 'P',
    4: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu1():
    for optionID in menu1_options.keys():
        print(optionID, '--', menu1_options[optionID] )
    runOptions()

# menu option 1
def s():
    print('You chose \' 1 -  S\'')

# menu option 2
def n():
    print('You chose \' 2 - N\'')
    
# menu option 3
def p():
    print('You chose \' 2 - P\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                print_menu2()
            elif option == 2:
                n()
            elif option == 3:
                p()
            # Exit menu    
            elif option == 4:  
                print('Exiting! Thank you! Goodbye!')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

"""
======================================================================
                         PATTERN FUNCTIONS
======================================================================
"""

#funcy.py
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    |\   ")
    print(sp + "    |/   ")
    print(SHIP_COLOR, end="")
    print(sp + "\__ |__/ ")
    print(sp + " \____/  ")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)
  print_menu2()

"""
======================================================================
                         MENU 2
======================================================================
"""

# Menu options as a dictionary
menu2_options = {
    1: 'Hello',
    2: 'Hola',
    3: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for optionID in menu2_options.keys():
        print(optionID, '--', menu2_options[optionID] )
    runOptions2()

# call functions based on input choice
def runOptions2():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                print('Working on the christmas tree. Be patient.')
                exit()
            elif option == 2:
                ship()
            # Exit menu    
            elif option == 3:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')



#On start, call the first menu
if __name__=='__main__':
    print_menu1()

