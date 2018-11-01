"""The main entry point of the program."""

import os
import requests

# snooker_api = dict(
#     event = requests.get('http://api.snooker.org/?e=398'),
#     match = requests.get('http://api.snooker.org/?e=397&r=1&n=5'),
#     player = requests.get('http://api.snooker.org/?p=1'),
#     events_in_season = requests.get('http://api.snooker.org/?t=5&s=2015'),
#     event_matches = requests.get('http://api.snooker.org/?t=6&e=398'),
#     ongoing_matches = requests.get('http://api.snooker.org/?t=7'),
#     player_season_matches = requests.get('http://api.snooker.org/?t=8&p=1&s=2015'),
#     event_players = requests.get('http://api.snooker.org/?t=9&e=403'),
#     pro_players = requests.get('http://api.snooker.org/?t=10&st=p&s=2015'),
#     rankings = requests.get('http://api.snooker.org/?rt=MoneyRankings&s=2015'),
#     round_info = requests.get('http://api.snooker.org/?t=12&e=403')
# )
#
# for key, value in snooker_api.items():
#     print(f'{key}:   {value.json()}')


class Menu:
    """Model a simple menu that provides many options to the user."""

    def __init__(self, options, name='generic menu'):
        """Initialize the main options of the menu and set its name."""
        # We pass options as a list and convert it to a dictionary starting from 1
        self.name = name

        options.append('Quit\n')
        self.options = dict(enumerate(options, start=1))

    def get_input(self):
        """Get user input."""
        answer = int(input('Please enter an option: ')) # the option is always a numerical value
        return answer

    def show_menu(self):
        """List all options and a shiny ascii art title."""
        print(f'{self.name}\n')

        for number, option in self.options.items():
            print(f"{number}. {option if type(option) is str else option['value']}")

    def add_submenu(self, suboptions, option=1):
        """Add a submenu with a main option provided."""
        main_option = self.options[option]

        suboptions.append('Go back')

        # The top-level option is now a dictionary consisting of its value and its submenu.
        self.options[option] = {
            'value': main_option,
            'submenu': dict(enumerate(suboptions, start=1))
        }

    def show_submenu(self, main_option):
        """Show a submenu of the provided main option."""
        if not self.options[main_option]['submenu']:
            print('This option has no submenu.')
            return

        for number, option in self.options[main_option]['submenu'].items():
            print(f"{number}. {option}")


def show_info():
    print('jsadjf')

menu = Menu(options=['Select this',
                     'Select that',
                     'No select this'],
            name='snooker general 1.0')

menu.add_submenu(suboptions=['what now',
                             'do not do this again'],
                 option=2)

def determine_options():
    """Determine what option the user chooses (considering all submenus)"""
    menu.show_menu()
    options = [menu.get_input()]

    # Get a suboption.
    if isinstance(menu.options[options[0]], dict):  # check to see if there is a submenu
        os.system('clear')

        menu.show_submenu(options[0])
        options.append(menu.get_input())

    return tuple(options)  # options are already chosen and thus immutable

def determine_action(options, funcs):
    """Perform a specific task based on user input."""
    main_option = options[0]

    if len(options) == 2:
        suboption = options[1]

        if suboption == list(funcs[main_option])[-1]:  # last option on submenus is go back
            os.system('clear')

            options = determine_options()
            funcs[main_option][suboption](options, funcs)

        funcs[main_option][suboption]()

    funcs[main_option]()



# while True:
#
#
#     if option not in menu.options.keys():
#         print("\nThat's not a valid option!")
#         break
#     elif option == len(menu.options):  # last option is always quit
#         break
#     else:
#         determine_action(option)  # to be implemented

# store main funcs in a dict

funcs = {
    1: show_info,
    2: {
        1: show_info,
        2: show_info,
        3: determine_action
    },
    3: show_info,
    4: quit
}

options = determine_options()
determine_action(options, funcs)
