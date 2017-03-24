from Calphascript_allatoms import *
import MDAnalysis as md
u=md.Universe("YOURFILE.GRO", "CRYSTAL_STRUCTURE.pdb")
computeDistCenterAxis(u, "CA_dist_crystal.dat")

#import Calphascript
#import MDAnalysis as md
#u = md.Universe("all_c_long_pro.gro","all_c_long_pro_short.xtc")
#Calphascript.computeDistCenterAxis(u, "CA_dist.dat",1,10)
