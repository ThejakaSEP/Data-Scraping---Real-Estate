# Data analysis and wrangling
import numpy as np
import pandas as pd
import random as rnd

#Visualization
import seaborn as sns
import matplotlib.pyplot as plt

#MachineLearning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


train_df=pd.read_csv('/Users/test/Documents/Data Sets/Titanic/train.csv')
test_df=pd.read_csv('/Users/test/Documents/Data Sets/Titanic/test.csv')

combine=[train_df,test_df]
# print(combine)

#print(train_df.columns.values)
# print(train_df.head())
# print(test_df.tail())

# print((train_df.info()))
#
# print("-"*40)
#
# print(test_df.info())

# print(train_df.describe())
# print(train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).mean())
    # .mean().sort_values(by='Survived', ascending=False)

print(train_df[['Sex','Survived']].groupby(['Sex'],as_index=False).mean())

# g = sns.FacetGrid(train_df, col='Survived')
# g.map(plt.hist,'Age',bins=20)
# plt.show()


# grid = sns.FacetGrid(train_df, col='Survived', row='Pclass', size=2.2, aspect=1.6)
# grid.map(plt.hist, 'Age', alpha=.5, bins=20)
# grid.add_legend();
# plt.show()

grid = sns.FacetGrid(train_df, row='Embarked', size=2.2, aspect=1.6)
grid.map(sns.pointplot,'Pclass','Survived','Sex', palette='deep')
grid.add_legend()
plt.show()