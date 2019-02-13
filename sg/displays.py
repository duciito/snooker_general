"""UI functions used to show info to the user."""

import os
from threading import Timer
from itertools import groupby

import funcs


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
    os.system('clear')

    if not matches:
        print('There are no matches currently played')

    print('\nAll matches currently played.\n')
    for event, matches in groupby(matches, key=lambda each: each['event']):
        print(f'---\n{event}\n---')

        for match in matches:
            print(f" * {match['player1']} -- {match['score1']}:{match['score2']} -- {match['player2']}")

    Timer(10, display_ongoing_matches).start()
