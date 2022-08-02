#Ash Dobrenen
import csv
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import mean
from numpy import std
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#ML models
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
#model evaluation
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
#this code runs machine learning algorithms 

#open and split dataset
df = pd.read_csv('dataset.csv')
data = df.values
x, y = data[:, :-1], data[:,-1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


#different models to see which is the best overall for what i want to do with it
modelTypes = []
modelTypes.append(LogisticRegression(solver='liblinear'))
modelTypes.append(SVC())
modelTypes.append(KNeighborsClassifier())
modelTypes.append(DecisionTreeClassifier())
modelTypes.append(RandomForestClassifier())
modelTypes.append(GaussianNB())

#running above modles
modelList = ['Logistic Regression', 'SVC', 'KNN', 'Decision Tree', 'Random Forest', 'Naive Bayes']
accuracyAll = []
AUCAll = []
confusionMatrixs = []

for model in modelTypes:
    model.fit(x_train, y_train)#need x and y inputs and outputs? features columns and code column?
    prediction = model.predict(x_test)
    accuracyAll.append(metrics.accuracy_score(y_test, prediction))
    x, y, _thresholds = metrics.roc_curve(y_test, prediction)
    AUCAll.append(round(metrics.auc(x, y),2))
    confusionMatrixs.append(confusion_matrix(y_test, prediction))
    #precision, recall, f1-score with classification report for the models
    print('Classification Report for '+modelList[modelTypes.index(model)])
    print(classification_report(y_test, prediction))
    

#plot a confusion matrix
fig = plt.figure(figsize = (18,10))
for i in range(len(confusionMatrixs)):
    cm = confusionMatrixs[i]
    model = modelList[i]
    sub = fig.add_subplot(2, 3, i+1, title=model)
    cmPlot = sns.heatmap(cm, annot=True, cmap = 'Blues_r')
    cmPlot.set_xlabel('Predicted Values')
    cmPlot.set_ylabel('Actual Values')
    
    
#accuracy and AUC
accAucDf = pd.DataFrame({'Model':modelList, 'Accuracy':accuracyAll, 'AUC':AUCAll})    
print(accAucDf)


