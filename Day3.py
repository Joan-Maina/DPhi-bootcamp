import pandas as pd

sma_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv")

# SUMMARY AND AGGEREGATE FUNCTIONS
#1. DESCRIBE() gives a summary of numerical columns or the specified columns
# print(sma_data['crime_rate'].describe())

# the columns with two or more words can be done as shown above
# print(sma_data.describe())

#Aggregate functions
# these are specific methods to get specific values
#mean() to get mean of columns
# print(sma_data.mean())

#unique() to get unique values of a specified columns
# print(sma_data.region.value_counts())

#value_counts() helps get the nmber of values with the each unique value

# print(sma_data.crime_rate.value_counts())

#SORTING
# This is a technique used to arrange values in ascending values in default or descending if ascending is set to false
# the last part chooses the number of the first values
# print(sma_data.sort_values(by = 'crime_rate', ascending=False)[:5])


#RENAMING helps change the names of columns
# print(sma_data.rename(columns = {'physicians': 'num_physicians'}))

#MISSING VALUES can be detected using isnull() or isna() and can be filled with fillna()
print(sma_data.isna().sum())