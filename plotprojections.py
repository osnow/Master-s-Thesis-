#!/usr/bin/python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm

script_name = sys.argv[0]
input_file = sys.argv[1]
refproj = sys.argv[2]

dframe = pd.read_table(input_file, delim_whitespace=True, header=None)
dframeref = pd.read_table(refproj, delim_whitespace=True, header=None)

fig = plt.figure()
ax1 = fig.add_subplot(111)
s = ax1.scatter(dframe.iloc[::2,2], dframe.iloc[::2,3], c=dframe.iloc[::2,1],
cmap=matplotlib.cm.viridis, s=3)
ax2 = fig.add_subplot(111)
ax2.scatter(dframeref.iloc[:,2], dframeref.iloc[:,3],s=7, c='k')
plt.text(10,0,'4NPQ')
plt.text(58,87,'4HFI')
plt.xlabel("PC1")
plt.ylabel('PC2')
#plt.title(str(sys.argv[1]).split('.')[0] + " PC Projections")
#plt.title('F238L closed to open PC projections')
plt.colorbar(s)
plt.savefig('../../Analysis/Figures/PCA/closed-open_dub.eps',format='eps',dpi=1200)
