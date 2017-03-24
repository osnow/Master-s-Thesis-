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
script_name = sys.argv[0]
top = sys.argv[1]
traj = sys.argv[2]
run = sys.argv[3]

u = Universe(top, traj)
H = HOLEtraj(u, cpoint=True, step=50, cvect=[0,0,1], endrad=10, executable="~/hole2/exe/hole")

if run == 'True':
    H.run()
    H.save(filename='hole.pickle')

else:
    import cPickle
    H.profiles = cPickle.load(open('hole.pickle'))

minrad = H.min_radius()
print minrad
plt.plot(minrad[:,0], minrad[:,1],':') #plots min rad vs time 
plt.title('Minimum pore radius vs time')
plt.xlabel('Time (ns)')
plt.ylabel(r'Min radius ($\AA$)')
plt.show()
H.plot(
#frames=[x for x in range(1,1351,100)], 
cmap=matplotlib.cm.summer)
