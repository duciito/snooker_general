"""Create the base functionality of the project."""

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

# for key, value in snooker_api.items():
#     print(f'{key}:   {value.json()}')

# events = requests.get('http://api.snooker.org/?t=5&s=2018')
# events = events.json()
#
# print(requests.get('http://api.snooker.org/?rt=MoneyRankings&s=2018').json())
# print(requests.get('http://api.snooker.org/?p=3').json())

def get_player(id):
    """Return a json data about a snooker player based on his ID."""
    player = requests.get('http://api.snooker.org/', params={'p': id})
    player = player.json()[0]  # the data consists of a single dictionary in a list

    return f"{player['FirstName']} {player['LastName']}"


def get_ranking_list(year=2018, limit=32):
    """Get season rankings to a certain position."""
    rankings = requests.get('http://api.snooker.org/?rt=MoneyRankings', params={'s': year}).json()
    formatted_rankings = {}

    # Fill a new dictionary with rankings in an ordered way.
    for ranked_player in rankings[:limit]:
        player_pos = ranked_player['Position']
        player_name = get_player(ranked_player['PlayerID'])
        formatted_rankings[player_pos] = player_name

    return formatted_rankings


print(get_ranking_list())
