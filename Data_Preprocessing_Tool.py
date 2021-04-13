import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset= pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values #features
y = dataset.iloc[:,-1].values  #Dependent values

print(x)
print(y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values==np.nan, strategy='mean')
imputer.fit(X[:,1:3])





