import csv
import matplotlib.pyplot as plt
import pandas as pd

with open(file="NSL_Regular_Season_Data.csv", newline='') as regular:
    reader = csv.reader(regular)
    regularSeason = list(reader)

with open(file="NSL_Metadata.csv", newline='') as info:
    reader = csv.reader(info)
    teamInfo = list(reader)

df = pd.read_csv('NSL_Regular_Season_Data.csv')

i = 1

teamList = []

team_data = {}

# Team list
while i < len(teamInfo):
    teamList.append([teamInfo[i][3]])
    i += 1

print(teamList)

# Identifying the team name
for team in teamList:
    teamName = team[0]
    goalsConceded = []
    shotsByOpposing = []

    # Identifying the colums relevant to the team match-ups (games)
    teamMatches = df[(df['HomeTeam'] == teamName) | (df['AwayTeam'] == teamName)]
    
    # Iterates over the rows of the DataFrame 'teamMatches' (which consists of the team match-ups)
    for index, row in teamMatches.iterrows():
        if row['HomeTeam'] == teamName: # team is home
            goalsConceded.append(row['AwayScore'])
            shotsByOpposing.append(row['Away_shots'])
        if row['AwayTeam'] == teamName: # team is away
            goalsConceded.append(row['HomeScore'])
            shotsByOpposing.append(row['Home_shots'])
    
    totalConceded = sum(goalsConceded)
    totalShotsAgainst = sum(shotsByOpposing)

    percentage = round((totalConceded / totalShotsAgainst) * 100, 2)

    team_data[teamName] = {'Goals Conceded': totalConceded, 'Shots Against': totalShotsAgainst, 'Conversion': percentage}

for team, data in team_data.items():
    print(f"Team: {team}")
    print(f"Goals Conceded: {data['Goals Conceded']}")
    print(f"Shots by Opposing Team: {data['Shots Against']}")
    print(f"Conversion (%): {data['Conversion']}\n")

team_df = pd.DataFrame.from_dict(team_data, orient='index', columns=['Goals Conceded', 'Shots Against', 'Conversion'])

team_df_sorted = team_df.sort_values(by='Conversion', ascending=True)

# Plotting
plt.figure(figsize=(10, 8))
plt.bar(team_df_sorted.index, team_df_sorted['Conversion'], color='Blue')
plt.xlabel('Team')
plt.xticks(rotation=45)
plt.ylabel('Defensive Efficiency Conversion (%)')
plt.title('Defensive Efficiency (Total Goals Conceded vs. Total Shots by Opposing Teams)')
plt.tight_layout()
plt.show()