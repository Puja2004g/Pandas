import pandas as pd

stuff = {
    'corporation': ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
    'employee': ['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'salary': [200, 220, 190, 130, 120, 150]
}

# stuff = {
#     'corporation': ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
#     'salary': [200, 220, 190, 130, 120, 150]
# }

my_df = pd.DataFrame(stuff)
# print(my_df)


# Group by corporation - return an object location in memory
company = my_df.groupby('corporation')
# sal = my_df.groupby('salary')
print(company)
# print(sal)

# sum
print(company.sum())

# mean
# print("Mean: " + "\n")
# works only on numerical data
# print(sal.mean())

# max
print(company.max())

# min
print(company.min())

# standard deviation
# print("Standard deviation: " + "\n")
# only work on numerical data
# print(sal.std())

# variance
# print("Variance: " + "\n")
# print(sal.var())

# count
print("Count: " + "\n")
print(company.count())


# describe the data
print("Description: " + "\n")
print(company.describe())

