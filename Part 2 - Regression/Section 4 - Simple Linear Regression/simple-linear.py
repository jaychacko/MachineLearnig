# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:39:02 2017

@author: JayAcer
"""


# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


#fitting linear regression to training set

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train,y_train)

#predicting the test set 

y_pred = regressor.predict(X_test)

#visualise data of trainig set results

#pyplot function
plt.scatter(X_train,y_train, color = "red")
y_predReal = regressor.predict(X_train)
plt.plot(X_train,y_predReal,color="blue")
plt.title('Salary vs Experiance (Training set)')
plt.xlabel('Years of Experiance')
plt.ylabel('Salary')
plt.show()

#visualizing test set results
plt.scatter(X_test,y_test, color = "red")
plt.plot(X_train,y_predReal ,color="blue")
plt.title('Salary vs Experiance (Training set)')
plt.xlabel('Years of Experiance')
plt.ylabel('Salary')
plt.show()