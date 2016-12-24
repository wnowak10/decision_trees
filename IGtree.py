import pandas as pd
import os 
import sys

seed=9
eps=sys.float_info.epsilon
os.chdir('/Users/wnowak/Desktop') # Provide the path here
df = pd.read_csv("df.csv")

