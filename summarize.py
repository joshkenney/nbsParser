import pandas as pd

"""
1. create 4 new cols for total count of s201, s202, s101, s102, s103
"""

def summarize():
    longfile = 'output/features.csv'
    df = pd.read_csv(longfile)
    print(df)
