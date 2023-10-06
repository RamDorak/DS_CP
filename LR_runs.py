import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_excel("Prediction_dataset.xlsx", sheet_name="INDvs")
print(data)

X = data[['Overs', 'RPO', 'Inns']]
y = data[['Runs']]
print(X,"\n", y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R-squared (R2) Score: {r2}")

new_data = pd.DataFrame({'Overs': [20], 'RPO': [9.25], 'Inns': [1]})
predicted_runs = model.predict(new_data)
print(f"Predicted Runs: {predicted_runs[0]}")

def predict_runs(overs, rpo, inns):
    new_data = pd.DataFrame({'Overs': [overs], 'RPO': [rpo], 'Inns': [inns]})
    predicted_runs = model.predict(new_data)
    return predicted_runs[0]