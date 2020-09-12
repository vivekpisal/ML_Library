import pandas as pd
import numpy as np
from scipy.stats import mode
import seaborn as sns
import matplotlib.pyplot as plt

#1
def median_imputation(df,variable):
	median=df[variable].median()
	df[variable]=df[variable].fillna(median).inplace=True

#2
def random_sampling(df,variable):
	df[variable+'_random']=df[variable]
	rs=df[variable].dropna().sample(df[variable].isnull().sum(),random_state=0)
	rs.index=df[df[variable].isnull()].index
	df.loc[df[variable].isnull(),variable+'_random']=rs
	#df=df.drop([variable],axis=1)

#3
def mean_imputation(df,variable):
	mean=df[variable].mean()
	df[variable]=df[variable].fillna(mean).inplace=True

#4
def mode_imputation(df,variable):
	mode(df[variable])
	df[variable]=df[variable].fillna(mode).inplace=True

#5
def caputure_nan(df,variable):
	df[variable_'nan']=np.where(df[variable].isnull(),1,0)
	df[variable].median()
	df[variable].fillna(df.variable.median(),inplace=True)
#6
def endof_distribution(df,variable):
	extr=df[variable].mean()+3*df[variable].std()
	df[variable+'_enddist']=df[variable].fillna(extr)
	median=df[variable].median()
	df[variable].fillna(median,inplace=True)

#7
def arbitrary_imputation(df,variable,arbit):
	df[variable+'_arbitrary']=df[variable].fillna(arbit)

#8
def frequent(df,variable):
    most_frequent_category=df[variable].mode()[0]
    df[variable].fillna(most_frequent_category,inplace=True)

#9
def add_variable(df,variable):
	df[variable]=np.where(df[variable].isnull(),1,df[variable])
	frequent=df[variable].mode()[0]
	df[variable].fillna(frequent,inplace=True)

#10
def most_frequent(df,variable):
	df[variable+'_newvar']=np.where(df[variable].isnull(),'Missing',df[variable])




 

