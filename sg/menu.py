"""Contains a simple Menu class used for interacting with the user."""

import os


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
            return None

        for number, option in self.options[main_option]['submenu'].items():
            print(f"{number}. {option}")

    def determine_options(self, dispatcher, post_action=False):
        """Determine what option the user chooses (considering all submenus)"""

        if post_action:
            print('\nHow would you like to proceed?\n', '1. Go back', '2. Quit', sep='\n')
            answer = int(input('\nPlease enter an option: '))

            if answer != 1:
                quit()
            else:
                os.system('clear')
                options = self.determine_options(dispatcher)
                self.determine_action(options, dispatcher)

        self.show_menu()
        options = [self.get_input()]

        # Get a suboption.
        if isinstance(self.options[options[0]], dict):  # check to see if there is a submenu
            os.system('clear')

            self.show_submenu(options[0])
            options.append(self.get_input())

        return tuple(options)  # options are already chosen and thus immutable

    def determine_action(self, options, dispatcher):
        """Perform a specific task based on user input."""
        main_option = options[0]

        if len(options) == 2:
            suboption = options[1]
            action = dispatcher[main_option][suboption]

            if suboption == list(dispatcher[main_option])[-1]:  # last option on submenus is go back
                os.system('clear')

                options = self.determine_options(dispatcher)
                self.determine_action(options, dispatcher)

            action()
            self.determine_options(dispatcher, post_action=True)
        else:
            action = dispatcher[main_option]
            action()
            self.determine_options(dispatcher, post_action=True)
