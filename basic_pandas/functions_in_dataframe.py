import pandas as pd

stuff = {
    'corporation': ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
    'employee': ['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'salary': [200, 220, 190, 130, 120, 150]
}

my_df = pd.DataFrame(stuff)
print(my_df)


def times1000(x):
    return format(x * 1000, ",d")


mul_1000 = my_df['salary'].apply(times1000)
print("Multiplied by 1000 values")
print(mul_1000)

mul_df = pd.DataFrame(mul_1000)
print("Returning dataframe for the multiplication")
print(mul_df)


# return last name
def namer(x):
    if x == 'John':
        return 'John Elder'
    else:
        return x


my_df2 = my_df['employee'].apply(namer)
print("Adding last name")
print(my_df2)

# using lamda function
mul = my_df['salary'].apply(lambda x: x*1000)
print("Printing using lambda function: ")
print(mul)


