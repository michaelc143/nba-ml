import pandas as pd

user_input = input("Enter the name that you want points per game for: ")

data = pd.read_csv('nba23boxscores/basic.csv')
# 1628369
# Replace 'desired_player_id' with the specific player ID you want
desired_player_name = user_input  # Replace with the actual player ID, currently jayson tatum

# Filter data for the desired player ID
player_data = data[data['name'] == desired_player_name]

# Display the DataFrame containing the player's data
print(player_data)

total_points = player_data['PTS'].sum()
total_games = len(player_data)
ppg = total_points / total_games
playoff_games = 0
if total_games > 82:
    playoff_games = total_games - 82

print(f'Player name: {desired_player_name}')
print(f'Total Points: {total_points}')
print(f'Total Games: {total_games}')
print(f'Playoff games: {playoff_games}')
print(f'Points Per Game (PPG): {ppg:.2f}')
