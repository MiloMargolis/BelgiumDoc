import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# read in data
df = pd.read_csv('Data News Sources.csv')

# drop the columns im not using
df.drop(['Unnamed: 0', 'date', 'text', 'url', 'Safety Index'], axis=1, inplace=True)
df.dropna(axis=0, inplace=True)

# one hot encoding
df = pd.get_dummies(df, columns=['queried_country'], drop_first=True)

# X and y
X_encoded = df.drop(columns=['source_country']) 
y = df['source_country']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# implement the random forest regressor
rf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)

# fit the model
rf.fit(X_train, y_train)

# Making predictions on the data
predictions = rf.predict(X_train)
predictions
 
