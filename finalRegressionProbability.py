import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from joblib import dump, load

# Load the dataset
team_data = pd.read_csv('cleaned_NSL_Regular_Season_Data_with_Categories.csv')

# Determine the winner of each game (1 if the Home team won, 0 if not)
result = []
for index, row in team_data.iterrows():
    # Ignoring the possibility of a tie for simplicity
    HomeWinner = 1 if row['HomeScore'] > row['AwayScore'] else 0
    result.append(HomeWinner)

# Add the new information to the DataFrame
team_data['Result'] = result

# Selection of features for the model
X = team_data.iloc[:, 17:41]  # Adjusted based on provided code
y = team_data['Result'].astype('int')

# Data preprocessing
sc = StandardScaler()
X_scaled = sc.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.20, random_state=1)

# Train the logistic regression model
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Save the classifier and scaler to disk for later use
dump(classifier, 'logistic_regression_model_probability.joblib')
dump(sc, 'standard_scaler_probability.joblib')

# Predict probabilities of the outcomes for the test dataset
y_pred_proba = classifier.predict_proba(X_test)
probabilities_of_home_win = y_pred_proba[:, 1]  # Probability of home win

# Create a DataFrame to display actual outcomes vs predicted probabilities
final_with_probabilities = pd.DataFrame({'Actual': y_test, 'Probability_Home_Win': probabilities_of_home_win})

# Display the DataFrame with actual outcomes and predicted probabilities
print(final_with_probabilities)

# Optionally, calculate and print the accuracy or other performance metrics
# Here's a simple way to calculate the percentage of correct predictions
y_pred = classifier.predict(X_test)
correct_predictions = np.sum(y_pred == y_test)
total_predictions = len(y_pred)
accuracy = (correct_predictions / total_predictions) * 100
print(f"Accuracy: {accuracy:.2f}%")