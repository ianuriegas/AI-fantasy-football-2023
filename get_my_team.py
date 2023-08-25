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
                temp_position = POSITION_MAP[entry["playerPoolEntry"]["player"]["defaultPositionId"]]
            elif "D/ST" in entry["playerPoolEntry"]["player"]["fullName"]:
                temp_position = "defense"
            else:
                # Default to "unknown" if position is not in POSITION_MAP
                temp_position = "unknown"
            
            player_info = {
                "name": entry["playerPoolEntry"]["player"]["fullName"],
                "id": entry["playerPoolEntry"]["player"]["id"],
                "position": temp_position,
                "injured": entry["playerPoolEntry"]["player"]["injured"],
                "week_proj_points": round(entry["playerPoolEntry"]["player"]["stats"][2]["appliedTotal"], 1),
                "season_avg_points": round(entry["playerPoolEntry"]["player"]["stats"][3]["appliedAverage"], 1),
                "team_id": entry["playerPoolEntry"]["player"]["proTeamId"],
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


if __name__ == "__main__":
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
