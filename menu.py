"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- America' )
    print('2 -- Belarus' )
    print('3 -- China' )
    print('4 -- Denmark' )
    print('5 -- Exit')
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'America',
    2: 'Belarus',
    3: 'China',
    4: 'Denmark',
    5: 'Exit'
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def america():
    print('You chose \' 1 -  America\'')

# menu option 2
def belarus():
    print('You chose \' 2 - Belarus\'')

# menu option 3
def china():
    print('You chose \'3 - China\'')

# menu option 4
def denmark():
    print('You chose \'3 - Denmark\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                america()
            elif option == 2:
                belarus()
            elif option == 3:
                china()
            elif option == 4:
                denmark()
            # Exit menu    
            elif option == 5:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()
