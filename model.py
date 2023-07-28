import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import HuberRegressor, PassiveAggressiveRegressor, TheilSenRegressor

def load_data(data_path, x_column, y_column):
    df = pd.read_csv(data_path)
    x = df[[x_column]]
    y = df[y_column]

    return x, y

def train_and_evaluate_model(X_train, X_test, Y_train, Y_test, model):
    model.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(Y_test, y_pred)
    print(f"Mean Squared Error({model.__class__.__name__}): {mse}")
    return mse

def test_models(data_path, x_column, y_column, models=None, test_size=0.4):
    X, Y = load_data(data_path, x_column, y_column)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size)

    if models is None:
        models = [
            RandomForestRegressor(),
            LinearRegression(),
            Ridge(),
            Lasso(),
            ElasticNet(),
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
    for model in models:
        mse = train_and_evaluate_model(X_train, X_test, Y_train, Y_test, model)
        mse_vals[model] = mse

    best_model = min(mse_vals, key=lambda k: mse_vals[k])
    print(f"\nThe min regression is {min(mse_vals.values())} using {best_model.__class__.__name__}")

# DRIVER CODE
data_path = 'data\CSV_Data\subject1_data_1200.csv'
x_column = 'PULSE'
y_column = 'ECG'

# Test all models using the default model list
test_models(data_path, x_column, y_column)

# Alternatively, you can specify a list of specific models to test
# models_to_test = [RandomForestRegressor(), LinearRegression(), SVR()]
# test_models(data_path, x_column, y_column, models=models_to_test)
