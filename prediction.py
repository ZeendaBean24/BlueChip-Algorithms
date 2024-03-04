import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

# 1 = home win, #0 = away win. 

# Load the saved logistic regression model
classifier_loaded = load('logistic_regression_model.joblib')

# Load the new dataset
new_team_data = pd.read_csv('Updated_NSL_Group_Games_Data.csv')

# Adjust the column selection to match the features used during training
# Ensure the order and nature of features match those used for training
# This example assumes the correct features in the new dataset are now at different indices
X_new = new_team_data.iloc[:,3:27]  # Replace with actual indices

# Load the scaler
scaler = load('standard_scaler.joblib')

# Apply scaling to the new dataset's features
X_new_scaled = scaler.transform(X_new)

# Make predictions with the loaded model
y_new_pred = classifier_loaded.predict(X_new_scaled)

# Add these predictions to your new_team_data DataFrame
new_team_data['Predicted_Result'] = y_new_pred

# Display the predictions
print(new_team_data[['Predicted_Result']])