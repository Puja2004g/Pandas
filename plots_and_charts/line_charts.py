import pandas as pd
from numpy.random import randn

random = randn(100, 4)
my_cols = ['mon', 'tues', 'wed', 'thurs']

my_df = pd.DataFrame(random, columns=my_cols)
print(my_df)

# create line chart
my_df.plot(kind="line")

# absolute value
my_df.abs().plot(kind="line")

# add line width
my_df.abs().plot(kind="line", lw=5)

# add grids
my_df.abs().plot(kind="line", grid=True)

# plot only one column
my_df['mon'].abs().plot(kind="line")

# chart multiple columns
my_df[['mon','tues']].abs().plot(kind="line")

# change chart size
my_df[['mon','tues']].abs().plot(kind="line", figsize=(5,5))

# add title
my_df[['mon','tues']].abs().plot(kind="line", title="My random data")

# add shading
my_df[['mon', 'tues']].abs().plot(kind="line", title="My random data", alpha=0.8)

# add/remove legend
my_df[['mon','tues']].abs().plot(kind="line", title="My random data", legend=False)

# another method
my_df.plot.line()
my_df.plot.line(title="My random data", grid = True, legend=False, alpha = 0.5, lw=5, figsize=(10,10))



