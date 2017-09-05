# Data Preprocessing Template

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('Data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# fixing missing values

from sklearn.preprocessing import Imputer

# nan is how table shows no data, we are using mean to replace
imputer = Imputer(missing_values="NaN",strategy='mean',axis=0)
# we are targetting only missing columsn which are only in index 2 and 3
#python indedx 1 and 3
imputer = imputer.fit(x[:,1:3])
x[:,1:3] =imputer.transform(x[:,1:3] )


#encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])

#onehot dummy variable
onehotencoder = OneHotEncoder(categorical_features = [0])
x=onehotencoder.fit_transform(x).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#spliting into traiing set and test set 

from sklearn.cross_validation import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,
                                                 random_state=0)

# feature scaling

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)