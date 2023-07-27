import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv('data\CSV_Data\subject1_data_1200.csv')
selected_channels = ['PULSE', 'ECG', 'EMG1']
data = df[selected_channels]

x = data[['PULSE', 'EMG1']]
y = data['ECG']

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.4)

clf = RandomForestRegressor()

clf.fit(X_train, Y_train)

y_pred = clf.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(Y_test, y_pred)
print(f"Mean Squared Error(Random Forest Regressor): {mse}")