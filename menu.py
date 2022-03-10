# Menu options as a dictionary
country_options = {
    1: 'America',
    2: 'Belarus',
    3: 'China',
    4: 'Denmark',
    5: 'Estonia',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in country_options.keys():
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
    print('You chose \'3 - Cisty\'')
    
# menu option 4
def denmark():
    print('You chose \'4 - Denmark\'')
    
# menu option 5
def estonia():
    print('You chose \'5 - Estonia\'')
