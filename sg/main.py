"""The main entry point of the program."""

import os
import requests

from menu import Menu

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

def determine_action(options, dispatcher):
    """Perform a specific task based on user input."""
    main_option = options[0]

    if len(options) == 2:
        suboption = options[1]
        action = dispatcher[main_option][suboption]

        if suboption == list(dispatcher[main_option])[-1]:  # last option on submenus is go back
            os.system('clear')

            options = determine_options()
            action(options, dispatcher)

        action()
    else:
        action = dispatcher[main_option]
        action()

dispatcher = {
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
determine_action(options, dispatcher)
