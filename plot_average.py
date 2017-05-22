#!/usr/bin/python

#reads in multiple .dat files for angles and just plots the average column from
#the dataframe - Titles need to be manually changed for each angle type. This
#could be changed to be more automated 

import sys
import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('ggplot')

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Plots average angles from different systems')
    parser.add_argument("filename", nargs="+")
    return parser.parse_args()

#plots a rolling mean to smooth lines - window can be changed to have more/less
def plot(fname,count):
    dframe = pd.read_table(fname, sep=' ', header=None, names=['Frame', 'AVG'], usecols=[0,1])
    x = dframe['Frame']
    #plt.scatter(0, dframe['AVG'][0],s=10,c=colors[count])
    plt.plot(x, pd.Series.rolling(dframe['AVG'],
    window=50,center=True).mean(), c=colors[count],linestyle=line[count],  #marker=linemark[count],
    )

colors = ['black','black','tab:red','tab:red','tab:red','tab:blue','tab:blue','tab:purple','tab:purple']
labels = ['Wild Type', 'I233T', 'F238L','I233T/F238L', 'I233T/F238L']
linemark = ['None','o','None','o','^','None','o','None','o']
line = ['-','--','-','--','-.','-','--','-','--']
count = 0
args = parse_args()

for f in args.filename:
    plot(f,count)
    #plot(f,labels[label])
    count += 1

plt.ylim([9,17]) #lim for dtwist
#plt.ylim([0,11]) #lim for htwist
#plt.ylim([0,7]) #lim for htilt
#plt.legend(loc="best")
plt.xlim([-10,1600])
plt.xlabel('Time (ns)')
plt.ylabel('Angle (degrees)')
plt.title("Closed to Closed")
plt.savefig('../Figures/4panel_figs/dtwist_C-C.eps',format='eps',dpi=1200,)

