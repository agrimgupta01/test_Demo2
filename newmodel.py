import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import datetime
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(secure_filename(f.filename))
        y = request.form.get('date')

    df = pd.read_csv(f.filename)
    df['created_at'] = pd.to_datetime(df.created_at, format='%d-%m-%Y')
    data = df['total_order_count']

    X = df['created_at']

    X_train, X_test, data_train, data_test = train_test_split(
        X, data, test_size=0.15)
    print(X_train)
    print(X_train.shape)
    A = X_train.values.reshape(-1, 1)
    B = X_test.values.reshape(-1, 1)
    print(A)
    print(A.shape)
    model = lgb.LGBMRegressor()
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

    z = pd.to_datetime(y, format='%Y-%m-%d')
    ans = model.predict(z)
    print(ans)
    return ans


if __name__ == '__main__':
    app.run(debug=True)


#predict_train = model.predict(A)

# Root Mean Squared Error on training dataset
#rmse_train = mean_squared_error(data_train, predict_train)**(0.5)
#print('\nRMSE on train dataset :', rmse_train)

#score1 = r2_score(data_train, predict_train)
#print('\nAccuracy Score :', score1)

#predict_test = model.predict(B)

# Root Mean Squared Error on testing dataset
#rmse_test = mean_squared_error(data_test, predict_test)**(0.5)
#print('\nRMSE on test dataset :', rmse_test)

#score2 = r2_score(data_test, predict_test)
#print('\nAccuracy Score :', score2)


# print('\n')
# print(model.predict(
#    [pd.to_datetime(['2022-05-30'], format='%Y-%m-%d').values.astype("float")]))
