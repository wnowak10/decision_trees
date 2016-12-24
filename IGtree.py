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