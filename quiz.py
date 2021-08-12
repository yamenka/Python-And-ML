import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

dataset = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv')
dataset.head() #prints the first 10 rows of my Dataframe just for testing
dataset.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean() # to get the lowest average fuel type cost per unit burned which is gas 
dataset.describe() # to get the std of fuel_mmbtu_per_unit --> 10.60 and 75th Percentile --> 17.01
dataset['fuel_qty_burned'].skew() #to get skewness of fuel qtn burned equals to 15.85
dataset['fuel_qty_burned'].kurtosis() # to get kurtosis of fuel qtn burned equals to 651.37
dataset.isna().sum() # to get the sum of missing values and the column this data is missing from which is fuel_unit and of total 180 
dataset.isnull().sum() * 100 / len(dataset) # to get the percentage of the missing data from the overall data equals to = 0.69 %
dataset.corr() # to get the 2nd and 3rd lowest correlation with fuel cost per unit burned 
pd.set_option('display.max_rows', 500)
dataset.groupby(['report_year','fuel_type_code_pudl'])['fuel_cost_per_unit_burned'].mean() # to get the percentage change in the fuel cost per unit burned in 1998 and 1994
                                                                                           # 1994 = 14984.572 1998 =  11902.597 
pd.set_option('display.max_rows', 500)
dataset.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()  #11140.19723948813 year 1997

