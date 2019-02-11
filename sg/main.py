import os

from menu import Menu


def show_info():
    print('jsadjf')


def determine_options(menu):
    """Determine what option the user chooses (considering all submenus)"""
    menu.show_menu()
    options = [menu.get_input()]

    # Get a suboption.
    if isinstance(menu.options[options[0]], dict):  # check to see if there is a submenu
        os.system('clear')

        menu.show_submenu(options[0])
        options.append(menu.get_input())

    return tuple(options)  # options are already chosen and thus immutable


def determine_action(options, menu, dispatcher):
    """Perform a specific task based on user input."""
    main_option = options[0]

    if len(options) == 2:
        suboption = options[1]
        action = dispatcher[main_option][suboption]

        if suboption == list(dispatcher[main_option])[-1]:  # last option on submenus is go back
            os.system('clear')

            options = determine_options(menu)
            action(options, menu, dispatcher)

        action()
    else:
        action = dispatcher[main_option]
        action()


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
        1: show_info,
        2: {
            1: show_info,
            2: show_info,
            3: determine_action
        },
        3: show_info,
        4: quit
    }

    options = determine_options(menu)
    determine_action(options, menu, dispatcher)


if __name__ == '__main__':
    main()

