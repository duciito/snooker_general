import funcs
from menu import Menu


def display_rankings(year=2018, limit=32):
    """Display player rankings."""

    rankings = funcs.get_rankings(year, limit)

    print(f'\nCurrent rankings for the {year} season.\n')
    for pos, player_name in rankings.items():
        print(f'{pos}. {player_name}')


def show_season_events(year=2018):
    """Show all season events."""

    events = funcs.get_season_events(year)

    print(f'\nAll events played in the current season.\n')
    for event in events:
        print(f" * {event['name']} (from {event['start_date']} to {event['end_date']})")


def display_ongoing_matches():
    """Display all matches played at the time this function is called."""

    matches = funcs.get_ongoing_matches()

    print(f'\nAll matches played currently.\n')
    for match in matches:
        print(f" * {match['player1']} -- {match['score1']}:{match['score2']} -- {match['player2']}")


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

    options = menu.determine_options()
    menu.determine_action(options, dispatcher)


if __name__ == '__main__':
    main()
