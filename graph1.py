import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('NSL_Regular_Season_Data.csv', newline='') as regularSeasonRawData:
    reader = csv.reader(regularSeasonRawData)
    regularSeasonData = list(reader)

regularSeasonData.pop(0)  # Remove headers

teamData = {}  # Initialize dictionary to store team data

# Process data to accumulate xG and shots for each team
for row in regularSeasonData:
    homeTeam = row[3]  # Assuming column index 3 for home team code
    awayTeam = row[4]  # Assuming column index 4 for away team code
    homeXG = float(row[6])  # Assuming column index 6 for home xG
    awayXG = float(row[7])  # Assuming column index 7 for away xG
    homeShots = int(row[8])  # Assuming column index 8 for home shots
    awayShots = int(row[9])  # Assuming column index 9 for away shots

    # Update home team data
    if homeTeam not in teamData:
        teamData[homeTeam] = {'totalXG': 0, 'matches': 0}
    teamData[homeTeam]['totalXG'] += homeXG
    teamData[homeTeam]['matches'] += 1

    # Update away team data
    if awayTeam not in teamData:
        teamData[awayTeam] = {'totalXG': 0, 'matches': 0}
    teamData[awayTeam]['totalXG'] += awayXG
    teamData[awayTeam]['matches'] += 1

# Calculate average xG for each team
for team in teamData:
    teamData[team]['avgXG'] = teamData[team]['totalXG'] / teamData[team]['matches']

# Convert teamData to DataFrame for plotting
teams = list(teamData.keys())
avgXGs = [teamData[team]['avgXG'] for team in teams]

df = pd.DataFrame({'Team': teams, 'Average xG': avgXGs})

# Plotting
plt.figure(figsize=(14, 6))
plt.bar(df['Team'], df['Average xG'], color='skyblue')
plt.xlabel('Team')
plt.ylabel('Average Expected Goals (xG)')
plt.title('Average xG per Team')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()