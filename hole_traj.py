#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.cm
import sys
from MDAnalysis.analysis.hole import HOLE, HOLEtraj
from MDAnalysis import Universe
script_name = sys.argv[0]
top = sys.argv[1]
traj = sys.argv[2]
run = sys.argv[3]
#last_frame = int(sys.argv[4])

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
plt.plot(minrad[:,0], minrad[:,1],':')
plt.title('Minimum pore radius vs time')
plt.xlabel('Time (ns)')
plt.ylabel(r'Min radius ($\AA$)')
plt.show()
H.plot(
#[x for x in range(1,801,50)]
cmap=matplotlib.cm.summer)
