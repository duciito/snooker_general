"""Contains a simple Menu class used for interacting with the user."""


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
