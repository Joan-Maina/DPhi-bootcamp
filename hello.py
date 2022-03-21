#  PANDAS(Python Data Analysis Library)
# Allows analysis, manipulation and exploring of large data with ease.
import pandas as pd
# Pandas has several objects Series: a one-dimensional labelled array

l = [1,1,2,3,5,8,13]
print(pd.Series(l))

# you can create your own series using dictionary
j = {'one' : 1, 'two' : 2, 'three':3}
print(pd.Series(j))

# python list, you can also use numpy array to create a dataFrame
data = [[1000,'joan',90],
[2000,'wanini',100],
[3000,'maina',100]]
print(pd.DataFrame(data))

# you can define the columns 
print(pd.DataFrame(data,columns=['Regd. No','Name','Marks%'],index=[1,2,3]))

# creating using dictionary
joan = {
        'numbers':[2,7,12],
    'names':['joan','wanini','maina'],
    'dreams':['be an awesome senior developer','be a good reader','be an excellent communicator']
}



print(pd.DataFrame(joan))

# sma_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv")
# print(sma_data.dtypes)

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

