import os
import json

# Path to the folder containing JSON files
folder_path = "data/team_data"

# Create empty lists for each position
qb_players = []
rb_players = []
wr_players = []
te_players = []
defense_players = []
kicker_players = []

# Iterate through each JSON file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            for player in data:
                position = player.get("position", "").lower()
                if position == "qb":
                    qb_players.append(player)
                elif position == "rb":
                    rb_players.append(player)
                elif position == "wr":
                    wr_players.append(player)
                elif position == "te":
                    te_players.append(player)
                elif position == "defense":
                    defense_players.append(player)
                elif position == "kicker":
                    kicker_players.append(player)

            print(json.dumps(qb_players, indent=4))
            qb_players = []
