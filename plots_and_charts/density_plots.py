import pandas as pd
from numpy.random import randn

random = randn(100, 4)
my_cols = ['mon', 'tues', 'wed', 'thurs']

my_df = pd.DataFrame(random, columns=my_cols)

# create a kernel estimation density (kde) plot
my_df.plot(kind="kde")

# another method for kde
my_df.plot.kde()

# create a density plot
my_df.plot.density()

# another method for density plot
my_df.plot(kind="density")

# change alpha/transparency
my_df.plot.kde(alpha=0.5,title="My random data")

# add line width
my_df.plot.kde(alpha=0.5,title="My random data", lw=10, grid=True)

# plot only one column
my_df['mon'].plot.kde(alpha=0.5,title="My random data")

