from understatapi import UnderstatClient
import pandas as pd
from matplotlib import pyplot as plt

understat = UnderstatClient()


# get data for every player playing in the Premier League in 2019/20
league_player_data = understat.league(league="EPL").get_player_data(season="2025")
player_data =pd.DataFrame(league_player_data)

player_data.head()

# Filter players from Chelsea
chelsea_players = player_data[player_data["team_title"] == "Chelsea"]
# Exclude players with 0 goals and 0 assists
chelsea_players = chelsea_players[(chelsea_players["goals"] > "1")]
# Plot xG vs x

plt.bar(chelsea_players["goals"],chelsea_players["player_name"])
plt.xlabel("xG")
plt.ylabel("xA")
plt.title("xG vs xA for Premier League Players (2025 Season)")
plt.show()
