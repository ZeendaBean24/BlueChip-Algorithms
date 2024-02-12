# Graph 1 - Expected Goals vs. Number of Shots (Quality of Shots)

# TODO: add it for each team, and a win/loss factor

import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('NSL_Regular_Season_Data.csv', newline='') as regularSeasonRawData:
    reader = csv.reader(regularSeasonRawData)
    regularSeasonData = list(reader)

regularSeasonData.pop(0)

regularSeasonProcessedData = []

i = 0
while i < len(regularSeasonData): 
    homeDivisionFactor = int(regularSeasonData[i][8])
    if homeDivisionFactor == 0:
        homeDivisionFactor = 1
    awayDivisionFactor = int(regularSeasonData[i][9])
    if awayDivisionFactor == 0:
        awayDivisionFactor = 1

    regularSeasonProcessedData.append([float(regularSeasonData[i][6]) / homeDivisionFactor, int(regularSeasonData[i][8]), float(regularSeasonData[i][7]) / awayDivisionFactor, int(regularSeasonData[i][9])]) #Home XG, Home Shots, Away XG, Away Shots
    i += 1

df = pd.DataFrame(regularSeasonProcessedData, columns = ["homeXG", "homeShots", "awayXG", "awayShots"])

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Home teams
ax[0].scatter(df['homeShots'], df['homeXG'], color='blue', label='Home Teams')
ax[0].set_xlabel('Shots')
ax[0].set_ylabel('Average Expected Goals (xG)')
ax[0].set_title('Home Teams Shot Quality: Shots vs AVerage xG')
ax[0].grid(True)

# Away teams
ax[1].scatter(df['awayShots'], df['awayXG'], color='red', label='Away Teams')
ax[1].set_xlabel('Shots')
ax[1].set_ylabel('Average Expected Goals (xG)')
ax[1].set_title('Away Teams Shot Quality: Shots vs Average xG')
ax[1].grid(True)

plt.tight_layout()
plt.show()