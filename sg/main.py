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

    def __init__(self, name='generic menu', options='No options have been added.'):
        """Initialize the main options of the menu and set its name."""
        # We pass options as a list and convert it to a dictionary starting from 1
        self.name = name
        self._options = dict(enumerate(options, start=1))

    def _get_input(self):
        """Get user input."""
        answer = int(input('Please enter an option: ')) # the option is always a numerical value
        return answer

    def show_menu(self):
        """List all options and a shiny ascii art title."""
        print(f'{self.name}\n')

        for number, option in self._options.items():
            print(f"{number}. {option if type(option) is str else option['value']}")
        print(f'{len(self._options.keys()) + 1}. Quit\n')

        self._get_input()

    def add_submenu(self, option=1, options='No options have been added.'):
        """Add a submenu with a main option provided."""
        main_option = self._options[option]

        # The top-level option is now a dictionary consisting of its value and its submenu.
        self._options[option] = {
            'value': main_option,
            'submenu': dict(enumerate(options, start=1))
        }

