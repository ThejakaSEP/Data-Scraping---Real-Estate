import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',None)
data=pd.read_csv('C:/Users/Vajira/Downloads/creditcard.csv')

#print(data.columns)

#print(data.shape)
# print(data.describe())
# print(data.shape)
print(data.head())
# data=data.sample(frac=0.1,random_state=1)
# print(data.shape)

#plot histogram for each parameter
# data.hist(figsize=(20,20))
# plt.show()

#Determine the number of Fraud cases

Fraud=data[data['Class']==1]
Valid=data[data['Class']==0]

outlier_fraction=len(Fraud)/float(len(Valid))
# print(outlier_fraction)

#Correlation Matrix
corrmat = data.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=0.8,square=True)
plt.show()

#get all the data from the data fram
columns = data.columns.tolist()

#filter the columns to remove the data we do not want
columns = [c for c in columns if c not in["Class"]]

#store the varialble we will be predicting on
target = "Class"

x=data[columns]
y=data[target]

#print the shapes
print(x.shape)
print(y.shape)

from sklearn.metrics import classification_report,accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

state = 1

#Define  outlier detection methods
classifiers = {
    "Isolation Forest": IsolationForest(max_samples=len(x),
                                        contamination=outlier_fraction,
                                        random_state=state),
    "Local Outlier Factor" : LocalOutlierFactor(
        n_neighbors=20,
        contamination=outlier_fraction)

}

#Fit the model

n_outliers=len(Fraud)

for i,(clf_name,clf) in enumerate(classifiers.items()):

    #fit the data and tag outliers

    if clf_name=="Local Outlier Factor" :
        y_pred = clf.fit_predict(x)
        scores_pred = clf.negative_outlier_factor_

    else :
        clf.fit(x)
        scores_pred = clf.decision_function(x)
        y_pred=clf.predict(x)

    #Reshape the prediction values to 0 for valid, 1 for fraud

    y_pred[y_pred==1] = 0
    y_pred[y_pred==-1] = 1

    n_errors = (y_pred!=y).sum()

    #run calssificaiton matrics
    print('{}: {}'.format(clf_name,n_errors))
    print(accuracy_score(y,y_pred))
    print(classification_report(y,y_pred))
