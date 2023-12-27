import pandas as pd

stuff = {
    'corporation': ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
    'employee': ['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'salary': [200, 220, 190, 130, 120, 150]
}

my_df = pd.DataFrame(stuff)
print(my_df)


def times10(x):
    return x * 10


mul_10 = my_df['salary'].apply(times10)
print(mul_10)


# apply changes to the current dataframe
print("Changed salary column")
my_df['salary'] = mul_10
print(my_df)


def namer(x):
    return "Hello " + x


# functions apply to multiple columns
print("Functions applied to multiple columns ")
print(my_df[['employee', 'corporation']].apply(namer))


# apply it to current dataframe
print("Modified dataframe")
my_df[['employee', 'corporation']] = my_df[['employee', 'corporation']].apply(namer)
print(my_df)




