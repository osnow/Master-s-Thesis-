#!/usr/bin/python

import sys
import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Plots average angles from different systems')
    parser.add_argument("filename", nargs="+")
    return parser.parse_args()


def plot(fname,label):
    dframe = pd.read_table(fname, sep=' ', header=None, names=['Frame', 'AVG'], usecols=[0,1])
    x = dframe['Frame']
    plt.plot(x, pd.Series.rolling(dframe['AVG'],
    window=40,center=True).mean(), linestyle=':', label=label)

labels = ['4NPQ WT pH4', '4NPQ WT pH7', '4NPQ BA2 pH4', '4NPQ I9T pH4', '4HFI pH4', '4HFI pH7', '4NPQ F238L pH4', '4NPQ I9T 2']
label = 0
args = parse_args()

for f in args.filename:
    plot(f,labels[label])
    label += 1

plt.legend(loc="best")
plt.xlabel('Time (ns)')
plt.ylabel('Angle (degrees)')
plt.title("Average Helix Tilt Angles vs Time")
plt.show()

