import pandas as pd
from numpy.random import randn

random = randn(100, 4)
my_cols = ['mon', 'tues', 'wed', 'thurs']

my_df = pd.DataFrame(random, columns=my_cols)
print(my_df)


# create a box plot
my_df.plot(kind="box")

# change plot size
my_df.plot(kind="box", figsize=(2,5))

# change color
my_df.plot(kind="box", cmap="jet")

# add legend
my_df.plot(kind="box", cmap="jet", legend=True)

# add title
my_df.plot(kind="box", cmap="jet", grid=True, title="My random data")

# another way
my_df.plot.box()
my_df.plot.box(title="My random data", grid=True, legend=True, cmap="jet", figsize=(5,5))




