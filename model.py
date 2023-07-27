import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import HuberRegressor, PassiveAggressiveRegressor, TheilSenRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('data\CSV_Data\subject1_data_1200.csv')
selected_channels = ['ECG', 'PULSE', 'PR']
data = df[selected_channels]

x = data[['PULSE', 'PR']]
y = data['ECG']

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.4)

# List of regression models to try
models = [
    RandomForestRegressor(),
    LinearRegression(),
    Ridge(),
    Lasso(),
    ElasticNet(),
    SVR(),
    DecisionTreeRegressor(),
    GradientBoostingRegressor(),
    KNeighborsRegressor(),
    GaussianProcessRegressor(),
    MLPRegressor(),
    HuberRegressor(),
    PassiveAggressiveRegressor(),
    TheilSenRegressor(),
]

mse_vals = {}

# Train and evaluate each model
for model in models:
    model.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(Y_test, y_pred)
    mse_vals[model] = mse
    print(f"Mean Squared Error({model.__class__.__name__}): {mse}")

print(f"The min regression is {min(mse_vals.values())} using {min(mse_vals, key=lambda k: mse_vals[k])}")