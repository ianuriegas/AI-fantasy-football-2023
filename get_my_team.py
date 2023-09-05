import requests
import os
import json
"""
Gets players from my team and puts them into a list
"""
teams = [
    {"league_id": 1431185954, "team_id": 4},
    {"league_id": 666403773, "team_id": 1},
    {"league_id": 1510308944, "team_id": 6},
    {"league_id": 2082362407, "team_id": 1},
    {"league_id": 1923771045, "team_id": 6},
    # {"league_id": 448465869, "team_id": 6}, # This league doesn't work for some reason
    {"league_id": 1542218952, "team_id": 7},
]


def make_league_data_json(league_id, team_id, data):
    # Create the data folder if it doesn't exist
    if not os.path.exists("data/league_data"):
        os.makedirs("data/league_data")

    # Construct the filename and path
    filename = f"data/league_data/LEAGUE-{league_id}-{team_id}.json"

    print(f"League data saved to {filename}")

    # Write the JSON data to the file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def get_players_list(league_id, team_id):
    url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/{league_id}?rosterForTeamId={team_id}&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        make_league_data_json(league_id, team_id, data)

        entries = data["teams"][team_id-1]["roster"]["entries"]

        player_list = []

        POSITION_MAP = {
            1: "qb",
            2: "rb",
            3: "wr",
            4: "te",
            5: "kicker",
            # Add more positions and IDs as needed
        }

        for entry in entries:
            if entry["playerPoolEntry"]["player"]["defaultPositionId"] in POSITION_MAP:
                temp_position = POSITION_MAP[entry["playerPoolEntry"]
                                             ["player"]["defaultPositionId"]]
            elif "D/ST" in entry["playerPoolEntry"]["player"]["fullName"]:
                temp_position = "defense"
            else:
                # Default to "unknown" if position is not in POSITION_MAP
                temp_position = "unknown"

            if entry["playerPoolEntry"]["player"]["injured"] is False:
                injured = 20
            else:
                injured = 0

            player_info = {
                "player_name": entry["playerPoolEntry"]["player"]["fullName"],
                # <------delete this line from the json in position_sorter.py
                "id": entry["playerPoolEntry"]["player"]["id"],
                # <------delete this line from the json in position_sorter.py || We need this to sort
                "position": temp_position,
                #     "injured": entry["playerPoolEntry"]["player"]["injured"],
                #     "week_proj_points": round(entry["playerPoolEntry"]["player"]["stats"][2]["appliedTotal"], 1),
                #     "season_avg_points": round(entry["playerPoolEntry"]["player"]["stats"][3]["appliedAverage"], 1),
                "team_id": entry["playerPoolEntry"]["player"]["proTeamId"],

                "opponent_defense_rank": 0,
                "team_offense_rank": 0,
                "weather_condition": 0,
                "days_since_last_game": 0,
                "avg_points": round(entry["playerPoolEntry"]["player"]["stats"][3]["appliedAverage"], 1),
                "is_home_game": 0,
                "injury_status": injured,
                "next_game_points": round(entry["playerPoolEntry"]["player"]["stats"][2]["appliedTotal"], 1)
            }

            # # Map position_id to position using POSITION_MAP
            # if "D/ST" in player_info["name"]:
            #     player_info["position"] = "defense"
            # elif player_info["position_id"] in POSITION_MAP:
            #     player_info["position"] = POSITION_MAP[player_info["position_id"]]
            # else:
            #     # Default to "unknown" if position is not in POSITION_MAP
            #     player_info["position"] = "unknown"

            player_list.append(player_info)

        return player_list

    else:
        print("Failed to fetch data from the URL")
        return []


def delete_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        #         print(f"Deleted: {file_path}")
        # print("All files in the folder have been deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_league_and_team_name(league_id, team_id):
    league_data_path = f"data/league_data/LEAGUE-{league_id}-{team_id}.json"
    with open(league_data_path, "r") as json_file:
        data = json.load(json_file)
        league_name = data['settings']['name']
        team_name = data['teams'][team_id-1]['name']
        # print(league_name)
        # print(team_name)
        return league_name, team_name

if __name__ == "__main__":
    paths = ["data/league_data", "data/team_data"]
    for path in paths:
        delete_files_in_folder(path)

    print("=================================================================================================================")
    for team in teams:
        league_id = team["league_id"]
        team_id = team["team_id"]
        print(f"League ID: {league_id}, Team ID: {team_id}")
        players_list = get_players_list(league_id, team_id)

        # Create the data folder if it doesn't exist
        if not os.path.exists("data/team_data"):
            os.makedirs("data/team_data")

        # Construct the filename and path
        filename = f"data/team_data/TEAM-{league_id}-{team_id}.json"
       
        # Write the JSON data to the file
        with open(filename, "w") as json_file:
            json.dump(players_list, json_file, indent=4)

        print(f"Team data saved to {filename}")
        print("=================================================================================================================")
