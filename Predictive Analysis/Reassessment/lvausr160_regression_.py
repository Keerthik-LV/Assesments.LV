# -*- coding: utf-8 -*-
"""LVAUSR160_Regression_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14AFabZpuUC2ePAFKs-a8ebbze-BIrHVy

**1. Data loading and initial checks**
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

df = pd.read_csv('/content/bengaluru_house_prices.csv')
df

"""**2. Data pre-processing**"""

df.isnull().sum()

"""**Imputation for missing values**"""

from sklearn.impute import KNNImputer
num_cols = df.select_dtypes(include=['int64','float64']).columns

imputing = KNNImputer()
for i in num_cols:
  df[i] = imputing.fit_transform(df[[i]])


# Handle string values in 'size' column
df['size'] = df['size'].apply(lambda x: np.mean([int(i) for i in x.split('-')]) if '-' in x else int(x))

# Display the updated 'size' column
print(df['size'])

df.isnull().sum()

categ_cols = df.select_dtypes(include='object').columns
categ_cols

"""**Duplicate check**"""

df.duplicated().sum()

"""**Data Overview**"""

df.describe(include='all')

df.shape

"""**3. Exploratory Data Analysis**

**Outlier detection**
"""

for i in num_cols:
  sns.boxplot(df[i])
  plt.show()

"""**Removal of outliers**"""

Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR
outlier = ((df[num_cols]<lower_bound) | (df[num_cols]>upper_bound)).any(axis=1)
df = df[~outlier]
df

df.shape

for i in num_cols:
  sns.boxplot(df[i])
  plt.show()

"""**Univariate Analysis**"""

for i in num_cols:
  sns.histplot(df[i])
  plt.show()

"""**Pairplot for Bivariate Analysis**"""

for col in num_cols:
    sns.histplot(df[col])
    plt.show()

"""**Heatmap for bivariate analysis**"""

sns.heatmap(df[num_cols].corr(),annot=True,cmap="Blues",fmt=".2f")

"""**Feature selection and encoding**"""

df = df.drop(columns=['area_type', 'availability', 'society', 'balcony', 'bath'])  # Drop irrelevant columns

"""**Datatype Check**"""

df.dtypes

le = LabelEncoder()
df['location'] = le.fit_transform(df['location'])
df['size'] = le.fit_transform(df['size'])
df['price'] = le.fit_transform(df['price'])

"""**Model training and evaluation**"""

X = df.drop(columns='price')
Y = df['price']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

from sklearn.preprocessing import StandardScaler

# Assuming the variables X_train, X_test, Y_train, and Y_test have been created

# Create a StandardScaler object
scaling = StandardScaler()

# Fit the scaler to the training data and transform it
X_train = scaling.fit_transform(X_train)

# Transform the test data using the same scaler
X_test = scaling.transform(X_test)

model = LinearRegression()
model.fit(X_train,Y_train)

y_pred = model.predict(X_test)

mean_squared_error(Y_test,y_pred)

r2_score(Y_test,y_pred)

rmse = np.sqrt(mean_squared_error(Y_test, y_pred))
rmse

from sklearn.metrics import mean_absolute_error

mean_absolute_error(Y_test,y_pred)

"""**6. Business Recommendations**

**Insights:**
The dataset was loaded and pre-processed, handling missing values and converting string values in the 'size' column to numerical values.

Outliers were detected and removed using the IQR method.

Univariate and bivariate analyses were conducted to understand the data distribution and relationships between variables.

Feature selection was performed by dropping irrelevant columns like 'area_type', 'availability', 'society', 'balcony', and 'bath'.

Encoding was applied to convert categorical variables like 'location', 'size', and 'price' to numerical values.

A Linear Regression model was trained and evaluated on the dataset, with metrics calculated for performance assessment.

**Recommendations:**
Feature Engineering: Explore additional feature engineering techniques to create new meaningful features that could enhance the model's predictive power.

**Advanced Modeling:** Consider exploring more advanced regression models like Random Forest Regressor or Gradient Boosting Regressor to potentially improve prediction accuracy.
Cross-Validation: Implement cross-validation techniques to ensure the model's generalizability and robustness.
"""