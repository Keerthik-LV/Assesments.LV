# -*- coding: utf-8 -*-
"""LVADUSR160_IA2_PA_1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p_eC7-lxMSWYOV1eFKckj3Y9y3Lrvm0S
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
# import statsmodels.api as sm

from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.cluster import KMeans

df=pd.read_csv('/content/Mall_Customers.csv')
df.head(10)

df.shape
df.info()
df.isnull().sum()
df.isnull().sum()/df.shape[0]*100

df.duplicated().sum()

df.describe()

for i in df.select_dtypes(include=['float64','int64']).columns:
  sns.histplot(df[i])
  plt.title(f'Histogram of {i}')
  plt.xlabel(i)
  plt.ylabel('Frequency')
  plt.show()

df['Spending Score (1-100)'].value_counts()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

for column in numerical_columns:
    plt.figure(figsize=(10, 6))  # Set the figure size for better readability
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

y_predict=model.predict(x_test)

accuracy_score(y_test,y_predict)