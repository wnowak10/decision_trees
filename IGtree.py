import pandas as pd
import os 
import sys

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