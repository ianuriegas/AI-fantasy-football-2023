import json
import re
from get_my_team import get_league_and_team_name
file_ = "data/league_data/LEAGUE-1431185954-4.json"
team_number = 4

# def get_league_and_team_name(team_id, file_path):
#     with open(file_path, "r") as json_file:
#         data = json.load(json_file)
#         league_name = data['settings']['name']
#         team_name = data['teams'][team_id-1]['name']
#         print(league_name)
#         print(team_name)

# get_league_and_team_name(team_number, file_)

# get_league_and_team_name("1431185954", 4)

def parse_json_filename(filename):
    pattern = r'TEAM-(\d+)-(\d+)\.json'
    match = re.match(pattern, filename)
    
    if match:
        league_id = match.group(1)
        team_id = match.group(2)
        return league_id, team_id
    else:
        return None, None
    

filename = 'TEAM-666403773-1.json'
league_id, team_id = parse_json_filename(filename)
print(f'League ID: {league_id}')
print(f'Team ID: {team_id}')