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
print(df)
print(df.dtypes)

# sort by categorical variable
cover = df.sort_values(by="Cloud cover")
print(cover)

#how many in cloud?
s=sum(df["Cloud cover"]=="Cloudy")

# split into two dfs. one is cloudy and one is not.
cover1, cover2 = cover[:s], cover[s:]


# find breakdowns
p1 = sum(cover1['Beverage']=="Coffee") / len(cover1)
p2 = sum(cover2['Beverage']=="Coffee") / len(cover2)

def entropy(p):
	return -p*(math.log(p+eps)/math.log(2))-(1-p+eps)*(math.log(1-p)/math.log(2))

# find entropy
print(entropy(p1))
print(entropy(p2 ))

#E0
entropy(sum(df["Beverage"]=="Tea")/len(df))

#E1
(len(cover1)/len(df))*entropy(p1) + (len(cover2)/len(df))*entropy(p2)