import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import datetime
from sklearn import preprocessing
from sklearn import utils
import csv


# with open("MLDATA.csv", 'r') as csvfile:
#df = csv.reader(csvfile)
# for x in df:
#    print(x)

df = pd.read_csv('MLDATA.csv', parse_dates=[
                 'created_at'], infer_datetime_format=True)
print(df)
#df['created_at'] = pd.to_datetime(df.created_at, format='%d-%m-%Y')
#Y = df['created_at'].values.astype('datetime64[ns]')
data = df['total_order_count']


X = df['created_at']
# print(df)
# print(X)
print(X.shape)
print(data.shape)

X_train, X_test, data_train, data_test = train_test_split(

    X, data, test_size=0.15)

A = X_train.values.reshape(-1, 1)
B = X_test.values.reshape(-1, 1)

model = LinearRegression()
model.fit(A, data_train)


predict_train = model.predict(A)

# Root Mean Squared Error on training dataset
rmse_train = mean_squared_error(data_train, predict_train)**(0.5)
print('\nRMSE on train dataset :', rmse_train)

score1 = r2_score(data_train, predict_train)
print('\nAccuracy Score :', score1)

predict_test = model.predict(B)

# Root Mean Squared Error on testing dataset
rmse_test = mean_squared_error(data_test, predict_test)**(0.5)
print('\nRMSE on test dataset :', rmse_test)

score2 = r2_score(data_test, predict_test)
print('\nAccuracy Score :', score2)
