#importing Numpy, Matplotlib and sklearn libraries
import matplotlib.pyplot as plt
import numpy as np
#importing datasets from scikit-learn
from sklearn import datasets, linear_model

#load the dataset
house_price = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
print(size)

#ReShape the input to your regression
size2 = np.array(size).reshape((-1, 1))
print(size2)

#By Using fit module in linear regression, user can fit the data frequently and quickly
regr = linear_model.LinearRegression()
regr.fit(size2, house_price)
print('Coefficients: \n', regr.coef_) #[251.92316258]
print('intercept: \n', regr.intercept_) #[251.92316258]

#Sample Output
size_new = 1400
#Example 1
price = (size_new * regr.coef_) + regr.intercept_
print(price)
#Example 2
print(regr.predict([[size_new]]))


#Formula obtained for the trained model
def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)

#Plotting the prediction line
graph('regr.coef_*x + regr.intercept_', range(1000, 2700))
plt.scatter(size, house_price, color = 'black')
plt.ylabel('House Price')
plt.xlabel('Size of lose in sq.ft.')
plt.show()

#My Notes:
"""
So, in SupervisedLearning, we have solution first, we trained it before we start putting it unknown data 
"""
