import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('NSL_Regular_Season_Data.csv', newline='') as regularSeasonRawData:
    reader = csv.reader(regularSeasonRawData)
    regularSeasonData = list(reader)

regularSeasonData.pop(0)  # Remove headers

regularSeasonProcessedData = []

# Process data and include match outcomes
for i in range(len(regularSeasonData)):
    homeDivisionFactor = int(regularSeasonData[i][8]) if int(regularSeasonData[i][8]) != 0 else 1
    awayDivisionFactor = int(regularSeasonData[i][9]) if int(regularSeasonData[i][9]) != 0 else 1
    homeScore = int(regularSeasonData[i][4])
    awayScore = int(regularSeasonData[i][5])
    
    # Determine match outcome
    if homeScore > awayScore:
        outcome = 'Home Win'
    elif homeScore < awayScore:
        outcome = 'Away Win'
    else:
        outcome = 'Draw'
    
    regularSeasonProcessedData.append([
        float(regularSeasonData[i][6]) / homeDivisionFactor,  # Home xG adjusted
        int(regularSeasonData[i][8]),  # Home shots
        float(regularSeasonData[i][7]) / awayDivisionFactor,  # Away xG adjusted
        int(regularSeasonData[i][9]),  # Away shots
        outcome  # Match outcome
    ])

df = pd.DataFrame(regularSeasonProcessedData, columns=["homeXG", "homeShots", "awayXG", "awayShots", "Outcome"])

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Define color map
color_map = {'Home Win': 'green', 'Away Win': 'red', 'Draw': 'yellow'}

scatterSize = 2

# Home teams
for outcome, color in color_map.items():
    subset = df[df['Outcome'] == outcome]
    ax[0].scatter(subset['homeShots'], subset['homeXG'], c=color, label=outcome, s=scatterSize)
ax[0].set_xlabel('Shots')
ax[0].set_ylabel('Average Expected Goals (xG)')
ax[0].set_title('Home Teams Shot Quality: Shots vs Average xG')
ax[0].grid(True)
ax[0].legend()

# Away teams
for outcome, color in color_map.items():
    subset = df[df['Outcome'] == outcome]
    ax[1].scatter(subset['awayShots'], subset['awayXG'], c=color, label=outcome, s=scatterSize)
ax[1].set_xlabel('Shots')
ax[1].set_ylabel('Average Expected Goals (xG)')
ax[1].set_title('Away Teams Shot Quality: Shots vs Average xG')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()