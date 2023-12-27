import pandas as pd
from numpy.random import randn

random = randn(100, 4)
my_cols = ['mon', 'tues', 'wed', 'thurs']

my_df = pd.DataFrame(random, columns=my_cols)
print(my_df)


# create a bar chart
my_df.plot(kind="bar")

# get absolute data
my_df.abs().plot(kind="bar")

# stack all bars together
my_df.abs().plot(kind="bar", stacked = True)

# add grids to the graph
my_df.abs().plot(kind="bar", grid = True, stacked=True)

# add shading
my_df.abs().plot(kind="bar", grid = True, stacked=True, alpha = 0.5)


# remove legend
my_df.abs().plot(kind="bar", grid = True, stacked=True,legend=False)

# add title
my_df.abs().plot(kind="bar", grid = True, stacked=True, title = "My random data")

# second method to create a bar chart
my_df.abs().plot.bar()
my_df.abs().plot.bar(grid = True, stacked=True, title = "My random data")