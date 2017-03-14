import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

script_name = sys.argv[0]
input_file = sys.argv[1]
#output_file = sys.argv[2]

names=['Frame','AVG','A','B','C','D','E','Min','Max']
dframe = pd.read_table(input_file, sep=' ', header=None, names=names)
dframe['Min'] = dframe.iloc[:,1:].min(axis=1)
dframe['Max'] = dframe.iloc[:,1:].max(axis=1)

fig, ax = plt.subplots()
x = dframe.loc[:,'Frame']
lines = [ax.plot(x, pd.Series.rolling(dframe.loc[:,i], window=15,center=True).mean(), ':')[0] for i in names[1:]]

leg = ax.legend(fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)
lined = dict()

for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(5)
    lined[legline] = origline

def onpick(event):
    legline = event.artist
    origline = lined[legline]
    vis = not origline.get_visible()
    origline.set_visible(vis)
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', onpick)

fig.suptitle('Helix Twist Angles')
plt.xlabel('Frame')
plt.ylabel('Angle')
plt.show()
