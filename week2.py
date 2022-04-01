from locale import normalize
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Assignment_Solutions/master/Standard%20Metropolitan%20Areas%20Data%20-%20train_data%20-%20data.csv")

# print(data.dtypes)

# seaborn is used to visualize using scatter, box, violin and other plots

sorted_nb = data.groupby(['physicians'])['hospital_beds'].median().sort_values()
# sns.boxplot(x=data['physicians'], y=data['hospital_beds'], order=list(sorted_nb.index))
sns.displot(data['hospital_beds'],x=data['physicians'],kind="kde")

# plt.show()

# double = lambda a,b:a if a > b else b
# print(double(7,12))