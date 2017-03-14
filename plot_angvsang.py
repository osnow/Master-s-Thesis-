#!/usr/bin/python

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Plots angle vs angle')
    parser.add_argument("file1")
    parser.add_argument("file2")
    return parser.parse_args()

args = parse_args()
dframe1 = pd.read_table(args.file1, sep=' ', header=None, names=['Frame', 'AVG'],
usecols=[0,1])
dframe2 = pd.read_table(args.file2, sep=' ', header=None, names=['Frame', 'AVG'],
usecols=[0,1])
print dframe1
print dframe2

#plt.plot(pd.Series.rolling(dframe1['AVG'], window=30,center=False).mean(),
#pd.Series.rolling(dframe2['AVG'], window=30,center=False).mean())
sns.regplot(dframe1['AVG'], dframe2['AVG'])
sns.plt.show()

