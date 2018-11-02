"""Create the base functionality of the project."""

import requests

snooker_api = dict(
    event = requests.get('http://api.snooker.org/?e=398'),
    match = requests.get('http://api.snooker.org/?e=397&r=1&n=5'),
    player = requests.get('http://api.snooker.org/?p=1'),
    events_in_season = requests.get('http://api.snooker.org/?t=5&s=2015'),
    event_matches = requests.get('http://api.snooker.org/?t=6&e=398'),
    ongoing_matches = requests.get('http://api.snooker.org/?t=7'),
    player_season_matches = requests.get('http://api.snooker.org/?t=8&p=1&s=2015'),
    event_players = requests.get('http://api.snooker.org/?t=9&e=403'),
    pro_players = requests.get('http://api.snooker.org/?t=10&st=p&s=2015'),
    rankings = requests.get('http://api.snooker.org/?rt=MoneyRankings&s=2015'),
    round_info = requests.get('http://api.snooker.org/?t=12&e=403')
)

for key, value in snooker_api.items():
    print(f'{key}:   {value.json()}')
