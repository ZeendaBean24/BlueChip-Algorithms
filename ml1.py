import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

team_data = pd.read_csv('NSL_Regular_Season_Data.csv')

#Determine the winner of each game (I am designating True (1) if the Home team won or False (0) if not)
result = []
for index,row in team_data.iterrows():
    #notice I am ignoring the possbility of a tie
    HomeWinner = 1 if row['HomeScore'] > row['AwayScore'] else 0
    result.append(HomeWinner)

#add the new information to the DataFrame
team_data['Result'] = result
print(team_data)

#I have arbitrarily chosen 3 columns as factors - Home Expected Goals, Away Expected Goals, Home ToP
X = team_data.iloc[:,[6,7,16]]
print (X)
y = team_data.iloc[:,21]
y = y.astype('int')

#this is where SciKit starts to do all of the work
sc = StandardScaler()
X = sc.fit_transform(X)
print (X)

# What happens if you alter test_size
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=1)
print (X_train.shape)
print (X_test.shape)
print (y_train.shape)
print (y_test.shape)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
final = pd.DataFrame({'Actual' : y_test, 'Predicted' : y_pred})

for index, row in final.iterrows():
    print(row['Actual'], row['Predicted'])

# Initialize counters
total_games = 0
correct_predictions = 0

# Iterate through each row in the DataFrame
for index, row in final.iterrows():
    total_games += 1  # Increment total games count
    if row['Actual'] == row['Predicted']:
        correct_predictions += 1  # Increment correct predictions count if actual equals predicted

# Calculate the percentage of correct predictions
percentage_correct = (correct_predictions / total_games) * 100

# Print the results
print(f"Total number of games: {total_games}")
print(f"Number of games predicted correctly: {correct_predictions}")
print(f"Percentage of correct predictions: {percentage_correct:.2f}%")