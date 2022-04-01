#  PANDAS(Python Data Analysis Library)
# Allows analysis, manipulation and exploring of large data with ease.
from locale import normalize
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

# Pandas has several objects Series: a one-dimensional labelled array

# l = [1,1,2,3,5,8,13]
# print(pd.Series(l))

# # you can create your own series using dictionary
# j = {'one' : 1, 'two' : 2, 'three':3}
# print(pd.Series(j))

# python list, you can also use numpy array to create a dataFrame
# data = [[1000,'joan',90],
# [2000,'wanini',100],
# [3000,'maina',100]]
# print(pd.DataFrame(data))

# you can define the columns 
# print(pd.DataFrame(data,columns=['Regd. No','Name','Marks%'],index=[1,2,3]))

# creating using dictionary
# joan = {
#         'numbers':[2,7,12],
#     'names':['joan','wanini','maina'],
#     'dreams':['be an awesome senior developer','be a good reader','be an excellent communicator']
# }



# print(pd.DataFrame(joan))

sma_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv")


# print(sma_data.loc[[1, 3, 5, 7, 9, 13],['land_area', 'work_force', 'income', 'region', 'crime_rate']])
# print(sma_data.loc[(sma_data['region'] == 4) & (sma_data['crime_rate'] == 55.64)])
# print(sma_data)
# print(sma_data[sma_data.region == 2])

# CSV files known as Comma-separated value can be read using read_csv that turns csv file to a dataframe
# a=pd.read_csv('transactions.csv')

# a dataframe can be converted back to a csv using to_csv
# b=a.to_csv('transactions2.csv')

# dataframes have function such as 
# 1. SHAPE
# It outputs: (no. of rows, no. of columns)
# print('the shape of our csv is:',a.shape)

# 2. HEAD 
# loads the first 5 values
# print(a.head())

# 3. TAIL
# loads the last 5 posts as default or no. of rows can be provided
# print(a.tail(2))

# 4. _DTYPES
# is used to get the datatype of an object's columns
# print(a.dtypes)

# 5. INFO
# is used to give details of the data
# print(a.info())




#DAY 3

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

# print(sma_data.land_area.value_counts())

#SORTING
# This is a technique used to arrange values in ascending values in default or descending if ascending is set to false
# the last part chooses the number of the first values
# print(sma_data.sort_values(by = 'crime_rate', ascending=False)[:5])


#RENAMING helps change the names of columns
# print(sma_data.rename(columns = {'physicians': 'num_physicians'}))

#MISSING VALUES can be detected using isnull() or isna() and can be filled with fillna()
# print(sma_data.isna().sum())



#DAY 4

 
 # create scatter plot and display
# plt.scatter(sma_data.crime_rate,sma_data.percent_senior)

# create a line plot 
# plt.plot(sma_data.land_area,sma_data.crime_rate)
# plt.xlabel('x-axis')
# plt.ylabel('y axis')
# plt.legend()
# plt.show()

#create a histogram
# plt.hist(sma_data.region)
# plt.show()

#create a correlation matrix
# print(sma_data.corr())

#create a bar plot
plt.hist(sma_data.income)
plt.show()
# or a horizontal bar plot
# plt.barh(sma_data.region, sma_data.crime_rate)

# pie charts
# firms = ["firm A","firm B","firm C","firm D","firm E"]
# market_share = [20,25,15,10,20]

# Explode = [0,0.1,0,0,0]
# plt.pie(market_share, explode=Explode,labels=firms, autopct='%1.1f%%')




#DAY 5
# two line graphs can be combined
# plt.plot(sma_data.work_force, sma_data.income, color="r", label='graph 1')
# plt.plot(sma_data.physicians, sma_data.income,label='graph 2', linestyle='dashed')

# more descriptions can be given
# plt.title('Joan')

# plt.show()


# several plots can be made together and displayed in a number of ways
# plt.subplot(1,2,1)
# plt.plot(sma_data.work_force, sma_data.income,"go")
# plt.title("Income vs work force")

# plt.subplot(1,2,2, sharey=True)
# plt.plot(sma_data.hospital_beds, sma_data.income,"rx")
# plt.title("Income vs hospital beds")
# plt.suptitle("sub plots")
# plt.show()


# DAY6
# DATA PRE-PROCESSING
# titanic_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/titanic_data.csv")

# median = titanic_data.isna()
# print(sma_data.isna().sum())

# x_train, x_test, ye_train, y_test = train_test_split(sma_data, test_size=0.20)

# x_train = normalize(x_train)
# x_test = normalize(x_test)