import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load your data from the specified sheet in the Excel file
excel_file = 'Prediction_dataset.xlsx'
sheet_name = 'FieldingFirst'
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Define features and target variable
features = ['RPO', 'Overs', 'Target']
target = 'Result'

X = data[features]
y = data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)

# Example prediction for a new data point
new_data_point = pd.DataFrame({
    'RPO': [5.54],
    'Overs': [50],
    'Target': [277],
})

predicted_result = model.predict(new_data_point)
print(f'Predicted Result: {predicted_result[0]}')