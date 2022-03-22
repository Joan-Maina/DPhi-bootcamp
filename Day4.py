import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sma_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv")
 
 # create scatter plot and display
# plt.scatter(sma_data.crime_rate,sma_data.percent_senior)

# create a line plot 
# plt.plot(sma_data.work_force,sma_data.income)

#create a histogram
# plt.hist(sma_data.percent_senior)

#create a bar plot
# plt.bar(sma_data.region, sma_data.crime_rate)
# or a horizontal bar plot
# plt.barh(sma_data.region, sma_data.crime_rate)


firms = ["firm A","firm B","firm C","firm D","firm E"]
market_share = [20,25,15,10,20]

Explode = [0,0.1,0,0,0]
plt.pie(market_share, explode=Explode,labels=firms, autopct='%1.1f%%')

plt.show()