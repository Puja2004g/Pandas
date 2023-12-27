import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('simple_dataframe.csv.csv')
print(data)
data.describe()

x = data['SAT']
y = data['GPA']

plt.scatter(x, y)
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()

X = sm.add_constant(x)
results = sm.OLS(y, X).fit()
results.summary()

plt.scatter(x,y)
yhat = 0.0017*x + 0.275
fig = plt.plot(x, yhat, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()

