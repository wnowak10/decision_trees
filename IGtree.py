#dtalg.py
from __future__ import division
import pandas as pd
import os 
import sys
import math
# import data
seed=9
eps=sys.float_info.epsilon
os.chdir('/Users/wnowak/Desktop') # Provide the path here
df = pd.read_csv("df.csv")


#what does df look like?
# print(df)
# print(df.dtypes)
# return variables in list
titles=df.columns.values

# define entropy function. use base 2. add eps so that we done get domain error from prob of 0. 
def entropy(p):
	return -p*(math.log(p+eps)/math.log(2))-(1-p)*(math.log(1-p+eps)/math.log(2))

#set initial max info gain at 0. see how much better we can do at this stage of tree
maxIG = 0
# find initial entropy. that is, what is entropy if we just tried to straight up classify label
# variable with no help
h_one = entropy(sum(df['Beverage']==df['Beverage'].unique()[0]) / len(df) )
# find len of dataframe. will need for entropy calcs.
l=len(df)
# for all feature columns
for i in range(len(df.columns)-1):
	# if feature is numerical, i'll want to see if i can deal with it a bit more efficiently 
	# than checking every outcome. some sort of algorithm that looks in top and bottom half to 
	# search for optimal split seems sensible. this remains to do
	if df[df.columns[i]].dtype == 'int64':
		# for each unique outcome. this is redundant when we have 2 categoricall variables, as it is going
		# to check for cloudy v not cloudy AND sunny v not sunny, when cloudy and not sunny are the same
		for j in range(len(df[df.columns[i]].unique())-1):
			print('int and i is and j is: ',i,j)
			num_df1 = df.loc[df[df.columns.values[i]] > df[df.columns[i]].unique()[j]]
			num_df2 = df.loc[df[df.columns.values[i]] <= df[df.columns[i]].unique()[j]]
			l1= len(num_df1)
			l2=len(num_df2)
			# these beverages should change to label variable in merged data set (features + label)
			print("l1 is ",l1)
			p1 = sum(num_df1['Beverage']==num_df1['Beverage'].unique()[0]) / l1
			p2 = sum(num_df2['Beverage']==num_df2['Beverage'].unique()[0]) / l2
			h_two = (l1/l)*entropy(p1) + (l2/l)*entropy(p2)
			IG = h_one - h_two
			if IG>maxIG:
				maxIG = IG
				print("found max IG at i and j",i,j,"and it is",maxIG)
	# if we have categorical data	
	else:
		for j in range(len(df[df.columns[i]].unique())):
			# split into two data frames
			print('cat and i and j is:',i,j)
			ddff = df.loc[df[df.columns.values[i]] == df[df.columns[i]].unique()[0]]
			ddff2 = df.loc[df[df.columns.values[i]] == df[df.columns[i]].unique()[1]]
			# how can i simply subtract ddff from df to get the other half of the split? thatd be ideal
			l1 = len(ddff)
			# these beverages should change to label variable in merged data set (features + label)
			p1 = sum(ddff['Beverage']==ddff['Beverage'].unique()[0]) / l1
			l2 = len(ddff2)
			p2 = sum(ddff2['Beverage']==ddff2['Beverage'].unique()[0]) / l2
			# weighted entropy for this split
			h_two = (l1/l)*entropy(p1) + (l2/l)*entropy(p2)
			IG = h_one - h_two
			print("found IG and it is",IG)
			if IG>=maxIG:
				maxIG = IG
				print("found max IG and it is",maxIG)


print(maxIG)
