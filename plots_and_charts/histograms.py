from numpy.random import randn
import pandas as pd

random = randn(100, 4)
my_cols = ['mon', 'tues', 'wed', 'thurs']

my_df = pd.DataFrame(random, columns=my_cols)
print(my_df)

# create a histogram
histogram = my_df['wed'].hist()
print(histogram)

# histogram with smaller bins
histogram2 = my_df['wed'].hist(bins=50)
print(histogram2)

# another way of creating histogram
histogram3 = my_df['wed'].plot(kind="hist", bins = 50)
print(histogram3)

# hist() methods
my_df.hist(bins=50, grid=False, legend=True)




