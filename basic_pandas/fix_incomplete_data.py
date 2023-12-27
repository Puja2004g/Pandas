import numpy as np
import pandas as pd

# create a dummy dataframe
stuff = {'a': [12, 13, 14], 'b': [15, np.nan, 67], 'c': [23, 16, 78], 'd': [34, 67, 28]}
my_df = pd.DataFrame(stuff)
print(my_df)

# delete a row with nan
my_df.dropna(inplace=True)

# delete columns with nan
my_df.dropna(axis=1, inplace=True)

# delete column with more than 1 null values
my_df.dropna(thresh=2, axis=1, inplace=True)

# replace null values
my_df.fillna(value=100, inplace=True)


# use math function in nan values
my_df.fillna(value=my_df['b'].mean(), inplace=True);

# use min
my_df.fillna(value=my_df['b'].min(), inplace=True)


# use max
my_df.fillna(value=my_df['b'].max(), inplace=True)


# use sum
my_df.fillna(value=my_df['c'].sum(), inplace=True)
print(my_df)



