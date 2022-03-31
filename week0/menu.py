from numpy import *
from week0 import keypad, menu, swap
from week1 import fibonacci, infodb
from week2 import Factorial, Palindrome, SquareRoot
""" 
======================================================================
                             MENU 1
======================================================================
"""

# # Menu options as a dictionary
# menu1_options = {
#     1: 'Patterns',
#     2: 'N',
#     3: 'S',
#     4: 'Exit',
# }

# # Print menu options from dictionary key/value pair
# def print_menu1():
#     for optionID in menu1_options.keys():
#         print(optionID, '--', menu1_options[optionID] )
#     runOptions()

# # menu option 1
# def patterns():
#     print('You chose \' 1 -  Patterns\'')

# # menu option 2
# def n():
#     print('You chose \' 2 - N\'')
    
# # menu option 3
# def s():
#     print('You chose \' 2 - S\'')


# # call functions based on input choice
# def runOptions():
#     # infinite loop to accept/process user menu choice
#     while True:
#         try:
#             option = int(input('Enter your choice 1-4: '))
#             if option == 1:
#                 print_menu2()
#             elif option == 2:
#                 n()
#             elif option == 3:
#                 s()
#             # Exit menu    
#             elif option == 4:  
#                 print('Exiting! Thank you! Goodbye!')
#                 exit() # exit out of the (infinite) while loop
#             else:
#                 print('Invalid option. Please enter a number between 1 and 4.')
#         except ValueError:
#             print('Invalid input. Please enter an integer input.')

"""
======================================================================
                         PATTERN FUNCTIONS
======================================================================
"""

# #funcy.py
# import time

# # terminal print commands
# ANSI_CLEAR_SCREEN = u"\u001B[2J"
# ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
# OCEAN_COLOR = u"\u001B[44m\u001B[2D"
# SHIP_COLOR = u"\u001B[32m\u001B[2D"
# RESET_COLOR = u"\u001B[0m\u001B[2D"

# def ocean_print():
#     # print ocean
#     print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
#     print("\n\n\n\n")
#     print(OCEAN_COLOR + "  " * 35)


# # print ship with colors and leading spaces
# def ship_print(position):
#     print(ANSI_HOME_CURSOR)
#     print(RESET_COLOR)
#     sp = " " * position
#     print(sp + "   |\    |\     ")
#     print(sp + "   |/    |/ ||  ")
#     print(SHIP_COLOR, end="")
#     print(sp + "\__|____ |__||____/ ")
#     print(sp + " \__o_TITANIC_o__/  ")
#     print(RESET_COLOR)


# # ship function, iterface into this file
# def ship():
#     # only need to print ocean once
#     ocean_print()

#     # loop control variables
#     start = 0  # start at zero
#     distance = 60  # how many times to repeat
#     step = 2  # count by 2

#     # loop purpose is to animate ship sailing
#     for position in range(start, distance, step):
#         ship_print(position)  # call to function with parameter
#         time.sleep(.1)
#   print_menu2()
  
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
    print(sp + "        |\   ")
    print(sp + "        |/   ")
    print(SHIP_COLOR, end="")
    print(sp + "\___ __ |____ __/ ")
    print(sp + " \_o_Titanic_o_/  ")
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
  
# christmas tree
def christmas():
  height = 11
  for i in range(height):
      print((' ' * (height - i)) + ('*' * ((2 * i) + 1)))
  print((' ' * height) + '|')

# keypad
matrix = [ [7,8,9],[4,5,6],[1,2,3],[" ","0"," "] ] 
def keypad():
  for i in matrix:
    for x in i:
      print(x,end = ' ')
    print()

# swap
def swap(a, b):
  if a > b:
      swap = a  # classic swap technique
      a = b
      b = swap
  return a, b
    
"""
======================================================================
                         MENU 2
======================================================================
"""

# # Menu options as a dictionary
# menu2_options = {
#     1: 'Christmas',
#     2: 'Titanic',
#     3: 'Keypad',
#     4: 'Swap',
#     5: 'Exit',
# }

# # Print menu options from dictionary key/value pair
# def print_menu2():
#     for optionID in menu2_options.keys():
#         print(optionID, '--', menu2_options[optionID] )
#     runOptions2()
    
# # menu option 1
# def christmas_option():
#     print('You chose \' 1 -  Christmas\'')

# # menu option 2
# def ship_option():
#     print('You chose \' 2 - Ship\'')

# # menu option 3
# def keypad_option():
#     print('You chose \' 3 - Keypad\'')

# # menu option 4
# def swap_option():
#     print('You chose \' 4 - Swap\'')


# # call functions based on input choice
# def runOptions2():
#     # infinite loop to accept/process user menu choice
#     while True:
#         try:
#             option = int(input('Enter your choice 1-5: '))
#             if option == 1:
#                 christmas_option()
#                 print("It's the most wonderful time of the year")
#                 christmas()
#                 # exit()
#             elif option == 2:
#                 ship_option()
#                 ship()
#             elif option == 3:
#                 keypad_option()
#                 keypad()
#             elif option == 4:
#                 swap_option()
#                 a = input("Choose a: ")
#                 b = input("Choose b: ")
#                 print(swap(a,b))
#             # Exit menu    
#             elif option == 5:  
#                 print('Exiting! Thank you! Good Bye...')
#                 exit() # exit out of the (infinite) while loop
#             else:
#                 print('Invalid option. Please enter a number between 1 and 3.')
#         except ValueError:
#             print('Invalid input. Please enter an integer input.')



main_menu = [
    ["N", n],
    ["S", s],
    # ["Loopy", loopy.main],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
# week1_sub_menu = [
#     ["Dictionaries", dictionaries.tester1],
#     ["Factorials", factorials.tester2],
#     ["Fibonacci", fibonacci.driver],
# ]

patterns_sub_menu = [
    ["Christmas", christmas],
    ["Titanic", ship],
    ["Keypad", keypad.driver],
    ["Swap", swap.driver],
]
Christmas',
    2: 'Titanic',
    3: 'Keypad',
    4: 'Swap',
    5: 'Exit
week2_sub_menu = [["Factorials using __call__", Factorial_with_call.driver],
                  ["Cube Root using Imperative and OOP", CubeRoot.driver]]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns", patterns_sub_menu])
#     menu_list.append(["Week 1", week1_submenu])
#     menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def patterns_submenu():
    title = "Patterns" + banner
    buildMenu(title, patterns_sub_menu)


# def week1_submenu():
#     title = "Week 1 Deliverables" + banner
#     buildMenu(title, week1_sub_menu)


# def week2_submenu():
#     title = "Week 2 Deliverables" + banner
#     buildMenu(title, week2_sub_menu)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice ==[ ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()

