from tabulate import tabulate

import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from sklearn import linear_model

def prediction(cases, x):
    A = np.array([np.arange(len(cases))]).T
    b = np.array([cases]).T
    lr = linear_model.LinearRegression()
    lr.fit(A,b)
    p = x*lr.coef_ + lr.intercept_
    return int(p[0][0])

def future2(name , species):
	res = []
	df = pd.read_csv(name)
	df['Year'] = pd.to_datetime(df['Year'])	
	for i in range(2022, 2031):
		res.append([i , prediction(df[species], i - 2006)])
	return res

