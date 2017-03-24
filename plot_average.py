#!/usr/bin/python

#reads in multiple .dat files for angles and just plots the average column from
#the dataframe - Titles need to be manually changed for each angle type. This
#could be changed to be more automated 

import sys
import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Plots average angles from different systems')
    parser.add_argument("filename", nargs="+")
    return parser.parse_args()

#plots a rolling mean to smooth lines - window can be changed to have more/less
def plot(fname,label):
    dframe = pd.read_table(fname, sep=' ', header=None, names=['Frame', 'AVG'], usecols=[0,1])
    x = dframe['Frame']
    plt.plot(x, pd.Series.rolling(dframe['AVG'],
    window=20,center=True).mean(), linestyle=':', label=label)

labels = ['4NPQ WT pH4', '4NPQ WT pH7', '4NPQ BA2 pH4', '4NPQ I9T pH4', '4HFI pH4', '4HFI pH7', '4NPQ F238L pH4', '4NPQ I9T 2']
label = 0
args = parse_args()

for f in args.filename:
    plot(f,labels[label])
    label += 1

plt.legend(loc="best")
plt.xlabel('Time (ns)')
plt.ylabel('Angle (degrees)')
plt.title("Average Domain Twist Angles vs Time")
plt.show()

