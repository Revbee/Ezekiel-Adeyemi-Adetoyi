#importing packages that might be needed
import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

#importing dataset and saving Data Set
url='https://github.com/WalePhenomenon/climate_change/blob/master/fuel_ferc1.csv?raw=true'
fuel_data = pd.read_csv(url, error_bad_lines=False)
fuel_data = pd.read_csv(url, error_bad_lines=False)

fuel_data.to_csv('fuel_data.csv', index=False)

#viewing the Structure of the Data
fuel_data

#grouping the data set by fuel type to investigate which has the lowest fuel cst
fuel_data.groupby('fuel_type_code_pudl').mean()

#Descriptive analysis to investigate in measure of dispersal 
fuel_data['fuel_mmbtu_per_unit'].describe()
fuel_data['fuel_qty_burned'].skew()

#investigating the magnitute of the Nan or missing values in the Data set
fuel_data.isnull().sum()

fuel_data.groupby('report_year').sum()
fuel_data.corr()
fuel_data.groupby('fuel_cost_per_unit_delivered').mean()