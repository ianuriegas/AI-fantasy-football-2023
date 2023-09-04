import os
import json
# from qb import get_qb_pytorch_stats
from rb import get_qb_pytorch_stats, get_rb_pytorch_stats, get_wr_pytorch_stats, get_te_pytorch_stats, get_kicker_pytorch_stats, get_defense_pytorch_stats
# Path to the folder containing JSON files
folder_path = "data/team_data"

# Create empty lists for each position
qb_players = []
rb_players = []
wr_players = []
te_players = []
defense_players = []
kicker_players = []

def print_pretty_json(title, data):
    print(f"{title}:")
    pretty_json = json.dumps(data, indent=4)
    print(pretty_json)


def get_combined_length(*arrays):
    total_length = sum(len(arr) for arr in arrays)
    return total_length

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

            # print(json.dumps(rb_players, indent=4))
            print("=================================================================================================================")
            # Getting the sorted data arrays
            qb_stats = get_qb_pytorch_stats(qb_players)
            rb_stats = get_rb_pytorch_stats(rb_players)
            wr_stats = get_wr_pytorch_stats(wr_players)
            te_stats = get_te_pytorch_stats(te_players)
            kicker_stats = get_kicker_pytorch_stats(kicker_players)
            defense_stats = get_defense_pytorch_stats(defense_players)

            # Printing pretty JSON format and calculating combined length
            # print_pretty_json("QB Stats", qb_stats)
            # print_pretty_json("RB Stats", rb_stats)
            # print_pretty_json("WR Stats", wr_stats)
            # print_pretty_json("TE Stats", te_stats)
            # print_pretty_json("Kicker Stats", kicker_stats)
            # print_pretty_json("Defense Stats", defense_stats)
            

            # combined_length = get_combined_length(qb_stats, rb_stats, wr_stats, te_stats, kicker_stats, defense_stats)
            # combined_length_2 = get_combined_length(qb_players, rb_players, wr_players, te_players, kicker_players, defense_players)
            # # print(f"Combined Length of All Arrays: {combined_length}")
            # print(len(qb_players))
            # print(len(rb_players))
            # print(len(wr_players))
            # print(len(te_players))
            # print(len(kicker_players))
            # print(len(defense_players))
            # print(f"Combined Length of All Arrays: {combined_length_2}")

            qb_players = []
            rb_players = []
            wr_players = []
            te_players = []
            kicker_players = []
            defense_players = []

print("=================================================================================================================")

# get_rb_pytorch_stats(test)
