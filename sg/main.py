from menu import Menu
from displays import *


def main():
    """The main entry point of the program."""
    menu = Menu(options=['Select this',
                         'Select that',
                         'No select this'],
                name='snooker general 1.0')

    menu.add_submenu(suboptions=['what now',
                                 'do not do this again'],
                     option=2)

    dispatcher = {
        1: display_ongoing_matches,
        2: {
            1: display_rankings,
            2: display_rankings,
            3: menu.determine_action
        },
        3: show_season_events,
        4: quit
    }

    options = menu.determine_options(dispatcher)
    menu.determine_action(options, dispatcher)


if __name__ == '__main__':
    main()
