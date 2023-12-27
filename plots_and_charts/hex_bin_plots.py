import pandas as pd
from numpy.random import randn

random = randn(100, 4)
my_cols = ['mon', 'tues', 'wed', 'thurs']

my_df = pd.DataFrame(random, columns=my_cols)
print(my_df)


# create hex bin plot
my_df.plot(kind="hexbin", x="mon", y="tues")

# add grid size
my_df.plot(kind="hexbin", x="mon", y="tues", gridsize=10)

# change color
my_df.plot(kind="hexbin", x="mon", y="tues", gridsize=10, cmap="Wistia")

# another method
my_df.plot.hexbin(x="mon", y="tues")

# add C offset
my_df.plot.hexbin(x="mon", y="tues", C="wed")
my_df.plot.hexbin(x="mon", y="tues",C="wed", gridsize=10, title="My random data",grid=True)

