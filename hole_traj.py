#!/usr/bin/python

#Uses MDanalysis package to calculate pore profiles and plot them - the
#calculation takes a long time so once it is done you can supply the command
#without the 'TRUE' argument to just make the plot from the pickle file
#you can uncomment the frames argument to plot specific frames for clarity

import matplotlib.pyplot as plt
import matplotlib.cm
import sys
from MDAnalysis.analysis.hole import HOLE, HOLEtraj
from MDAnalysis import Universe
import numpy as np
import pandas as pd 

script_name = sys.argv[0]
top = sys.argv[1]
traj = sys.argv[2]
run = sys.argv[3]

u = Universe(top, traj)
H = HOLEtraj(u, cpoint=True, step=25, cvect=[0,0,1], endrad=9, executable="~/hole2/exe/hole")

if run == 'True':
    H.run()
    H.save(filename='hole.pickle')

else:
    import cPickle
    H.profiles = cPickle.load(open('hole.pickle'))

minrad = H.min_radius()
I9 = []
for q, profile in H:
    d = {'radius':profile.radius, 'coord':profile.rxncoord}
    data = pd.DataFrame(d)
    I9.append(data['radius'][data['coord'].between(56,65,inclusive=True)].min())

plt.plot(minrad[:,0], pd.Series.rolling(pd.Series(I9), window=3,center=False).mean()) #plots min rad of I9 region vs time 
#plt.title('Minimum pore radius vs time')
plt.xticks(np.arange(0,1100,100))
plt.xlabel('Time (ns)')
plt.ylabel(r'Min radius ($\AA$)')
plt.savefig('../Figures/Hole_profiles/minrad_4HFI_WT_pH7.eps',format='eps',dpi=1200)
plt.close()
#title = str(sys.argv[4])
#H.plot(path='../Figures/Hole_profiles/4HFI_I9T_pH7.eps',frames=[x for x in range(1,len(minrad)*50,100)],cmap=matplotlib.cm.summer)
#plt.savefig('../Figures/Hole_profiles/4HFI_WT_pH46.eps',format='eps',dpi=1200)
