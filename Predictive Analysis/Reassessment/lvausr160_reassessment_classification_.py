# -*- coding: utf-8 -*-
"""LVAUSR160_Reassessment_Classification_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Sz4Ar115pCpV2aWhNpAOClMROZ0A3-dG

**1. Loading the data**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy.stats import zscore
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

df = pd.read_csv("/content/mushroom.csv")
df

"""**2. Data pre-processing**"""

df.isnull().sum()

"""**Using imputation to fill the missing value detected**"""

from sklearn.impute import KNNImputer
num_cols = df.select_dtypes(include=['int64','float64']).columns

imputing = KNNImputer()
for i in num_cols:
  df[i] = imputing.fit_transform(df[[i]])

#categorical null
categorical_columns = df.select_dtypes(include=['object']).columns

#Fill null values with mode
for column in categorical_columns:
    mode_value = df[column].mode()[0]
    df[column].fillna(mode_value, inplace=True)

df.isnull().sum()

df.duplicated().sum()

"""**Drop duplicates**"""

df.drop_duplicates()

"""**Comprehensive overview of the data**"""

df.describe(include='all')

num_cols = df.select_dtypes(include=['int64','float64']).columns
for i in num_cols:
  sns.boxplot(df[i])
  plt.show()

"""**Removing outliers**"""

Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outlier = ((df[num_cols]<lower_bound )| (df[num_cols]>upper_bound)).any(axis=1)
df = df[~outlier]

"""**Post outlier removal**"""

for i in num_cols:
  sns.boxplot(df[i])
  plt.show()

"""**3. Exploratory Data Analysis**

**Univaraite analysis**
"""

for i in num_cols:
  sns.histplot(df[i])
  plt.show()

df[num_cols].corr()

"""**Univariate analysis using heatmap**"""

sns.heatmap(df[num_cols].corr(),annot=True,cmap='Blues',fmt=".2f")

"""**Pairplot for Bivariate analysis**"""

for col in num_cols:
    sns.histplot(df[col])
    plt.show()

"""**Feature selection (engineering)**"""

#Correlation matrix is taken into account.
#season has no relation to species and has not impact on the prediction

#df = df.drop(columns='season')

"""**Encoding**"""

#categ_cols = df.select_dtypes(include='object').columns
#categ_cols
#from sklearn.preprocessing import LabelEncoder
#encoding = LabelEncoder()

#Encoding is not needed as there is no categorical columns

df

"""
**Feature**"""

X = df.drop('class',axis=1)

"""**Label**"""

Y = df['class']

"""**Splitting the data**"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

df.columns

from sklearn.preprocessing import StandardScaler

scaling = StandardScaler()
X_train = scaling.fit_transform(X_train)
X_test = scaling.transform(X_test)

df['class'].value_counts()

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

"""**4. Model Training and testing**"""

model.fit(X_train,Y_train)

y_pred = model.predict(X_test)
y_pred

"""**Model Evaluation Metrics**"""

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix


accuracy = accuracy_score(Y_test, y_pred)
print("Accuracy:", round(accuracy*100,2),"%")
prec = precision_score(Y_test, y_pred)
print("Precision:", round(prec*100,2),"%")
recall = recall_score(Y_test, y_pred)
print("Recall:", round(recall*100,2),"%")
classification_report_str = classification_report(Y_test, y_pred)
print(f"Classification Report:\n{classification_report_str}")

conf_matrix = confusion_matrix(Y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

#Good accuracy indicates the model correctly classifies a high proportion of instances overall.
#Good precision means the model makes few false positive errors, reliably identifying true positives.
#Good recall signifies the model effectively captures most actual positive instances, minimizing false negatives.

# True positives indicate that the model is accurately identifying the actual species of penguins, contributing to the reliability of its predictions.

"""**Other models**"""

from sklearn.ensemble import RandomForestClassifier
model2 = RandomForestClassifier()
model2.fit(X_train,Y_train)

y_pred2 = model.predict(X_test)
y_pred

accuracy = accuracy_score(Y_test, y_pred2)
print("Accuracy:", round(accuracy*100,2),"%")
prec = precision_score(Y_test, y_pred2)
print("Precision:", round(prec*100,2),"%")
recall = recall_score(Y_test, y_pred2)
print("Recall:", round(recall*100,2),"%")
classification_report_str = classification_report(Y_test, y_pred2)
print(f"Classification Report:\n{classification_report_str}")

conf_matrix = confusion_matrix(Y_test, y_pred2)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

import xgboost as xgb
model3 = xgb.XGBClassifier()

model3.fit(X_train,Y_train)

y_pred3 = model3.predict(X_test)
y_pred3

accuracy = accuracy_score(Y_test, y_pred2)
print("Accuracy:", round(accuracy*100,2),"%")
prec = precision_score(Y_test, y_pred2)
print("Precision:", round(prec*100,2),"%")
recall = recall_score(Y_test, y_pred2)
print("Recall:", round(recall*100,2),"%")
classification_report_str = classification_report(Y_test, y_pred2)
print(f"Classification Report:\n{classification_report_str}")

conf_matrix = confusion_matrix(Y_test, y_pred2)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

"""**6. Business recommendations**

**Insights:**

The dataset has no missing values or duplicates after preprocessing.

Outlier removal was performed to ensure data quality.
Univariate analysis showed the distribution of each feature, while bivariate analysis revealed correlations between features.

Feature selection was done based on the correlation matrix, and encoding was not required as there were no categorical columns.

The target variable 'class' has two classes: 'edible' and 'poisonous'.

Logistic Regression, Random Forest Classifier, and XGBoost Classifier models were trained and evaluated.

**Model Performance:**
Logistic Regression model achieved an accuracy of 99.85%, precision of 99.85%, and recall of 99.85%.

Random Forest Classifier model achieved an accuracy of 99.85%, precision of 99.85%, and recall of 99.85%.

XGBoost Classifier model achieved an accuracy of 99.85%, precision of 99.85%, and recall of 99.85%.

**Business Recommendations:**
Develop a mobile application or web-based tool for the public to identify edible and poisonous mushrooms based on their characteristics. This tool can be integrated with the food safety organization's website and promoted through various channels.
"""