import pandas as pd
from numpy.random import randn

random = randn(100, 4)
my_cols = ['mon', 'tues', 'wed', 'thurs']

my_df = pd.DataFrame(random, columns=my_cols)
print(my_df)

# create a scatter plot
my_df.plot(kind="scatter", x="mon", y="tues")

# add another offset
my_df.plot(kind="scatter", x="mon", y="tues", c="wed")

# add color
my_df.plot(kind="scatter", x="mon", y="tues", c="wed", cmap="magma")

# change size
my_df.plot(kind="scatter", x="mon", y="tues", s=my_df['wed']*30)

# shading/add transparency
my_df.plot(kind="scatter", x="mon", y="tues", alpha=0.5)

# add title
my_df.plot(kind="scatter", x="mon", y="tues", alpha=0.5, title="My random data", grid=True)

