import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

# Load the saved logistic regression model
classifier_loaded = load('logistic_regression_model_probability.joblib')

# Load the new dataset
new_team_data = pd.read_csv('Updated_NSL_Knockout_Round_Games.csv')

# Adjust the column selection to match the features used during training
# Ensure the order and nature of features match those used for training
# This example assumes the correct features in the new dataset are now at different indices
X_new = new_team_data.iloc[:,3:25]  # Adjust indices as necessary

# Load the scaler
scaler = load('standard_scaler_probability.joblib')

# Apply scaling to the new dataset's features
X_new_scaled = scaler.transform(X_new)

# Predict probabilities with the loaded model
y_new_pred_proba = classifier_loaded.predict_proba(X_new_scaled)

# Extract the probability of the home team winning
probability_home_win = y_new_pred_proba[:, 1]

# Add these probabilities to your new_team_data DataFrame
new_team_data['Probability_Home_Win'] = probability_home_win

# Display the DataFrame with probabilities
print(new_team_data[['Probability_Home_Win']])