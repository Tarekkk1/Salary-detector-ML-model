# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('D:/ML Courses/Machine Learning Datasets/Part 2 - Regression/Section 4 - Simple Linear Regression/Python/Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)


#fitting the simple linear regression to traning set
from sklearn.linear_model import LinearRegression
regressor =LinearRegression()
regressor.fit(x_train, y_train)

#predictiong the test set 
y_predect=regressor.predict(x_test)


#visualising the traning set results
plt.scatter(x_train, y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title("salary vs experiance (traing set")
plt.xlabel("years of expaiances")
plt.ylabel("Salarys")
plt.show()


#visualising the test set results
plt.scatter(x_test, y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title("salary vs experiance (test set")
plt.xlabel("years of expaiances")
plt.ylabel("Salarys")
plt.show()