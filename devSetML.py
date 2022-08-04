#Ash Dobrenen
import csv
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import mean
from numpy import std
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split, cross_validate
import matplotlib.pyplot as plt
#ML models
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import statistics
#model evaluation
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
#hyperparamter tuning libraries
import skopt
"""
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
"""
from sklearn.model_selection import RandomizedSearchCV


def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print (accuracy)
    print(confusion_matrix(y_test,y_pred))
    



#open and split dataset into train, development, and testing
df = pd.read_csv('dataset.csv')
data = df.values
X, y = data[:, :-1], data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
#splitting off a development/validation set
#X_train, X_devTest, y_train, y_devTest = train_test_split(X_train, y_train, test_size=0.25, random_state=1)

# Number of trees in random forest
n_estimators = [int(x) for x in range(200,2000,200)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestClassifier()
# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 75, cv = 3, verbose=2, random_state=42)
# Fit the random search model
rf_random.fit(X_train, y_train)
best_random = rf_random.best_estimator_
evaluate(best_random, X_test, y_test) 


print(rf_random.best_params_)
print("Dev set")
#prediction = rf_random.predict(X_devTest)
#print(classification_report(y_devTest, prediction))
print("test set")
prediction2 = rf_random.predict(X_test)
print(classification_report(y_test, prediction2))
