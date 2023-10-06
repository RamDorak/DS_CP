import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load your data from the specified sheet in the Excel file
excel_file = 'Prediction_dataset.xlsx'
sheet_name = 'FieldingFirst'
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Prompt the user to enter the Country playing against India
# country = input("Enter the Country playing against India: ")
country = ""
opposition = "v\xa0"+ country
print(opposition)

# Filter the dataset based on the entered country
filtered_data = data[data['Opposition'].str.contains(opposition)]
# Define features and target variable
features = ['RPO', 'Overs', 'Target']
target = 'Result'

X = filtered_data[features]
y = filtered_data[target]

if X.empty:
    print(f"No matches found for {country} against India in the dataset.")
else:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's performance
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Print the accuracy and classification report
    print(f'Accuracy: {accuracy:.2f}')
    print('Classification Report:')
    print(report)

    # Example prediction for a new data point
    new_data_point = pd.DataFrame ({
        'RPO': [5.2],
        'Overs': [49.5],
        'Target': [265],
    })

    # Make a prediction for the new data point
    predicted_result = model.predict(new_data_point)
    print(f'Predicted Result: {predicted_result[0]}')
    
def winloss(country, RPO, Overs, Target):
    opposition = "v\xa0"+ country
    global filtered_data
    filtered_data = data[data['Opposition'].str.contains(opposition)]
    new_data = pd.DataFrame({'RPO': [RPO], 'Overs':[Overs], 'Target': [Target]})
    winloss = model.predict(new_data)
    return winloss
    