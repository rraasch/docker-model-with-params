from sklearn.linear_model import LinearRegression
import pandas as pd
import json
import scipy.stats as s
import joblib

x0 = pd.Series(s.norm.rvs(loc=5, scale = 3, size = 1000, random_state = 1), name = 'x0')
x1 = pd.Series(s.norm.rvs(loc=2, scale = 2, size = 1000, random_state = 2), name = 'x1')

features = pd.concat([x0, x1], axis = 1)

target = x0+2*x1+pd.Series(s.norm.rvs(loc=1, scale = 1, size = 1000, random_state = 3))

lr = LinearRegression()
lr.fit(features, target)

joblib.dump(lr, "./model/lr.joblib")