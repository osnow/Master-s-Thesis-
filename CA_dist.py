from Calphascript_allatoms import *  #imports functions from other script
import MDAnalysis as md

# parse files - .tpr, .xtc, output.dat
def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file1")#, type=argparse.FileType('r'))
    parser.add_argument("file2")#, type=argparse.FileType('r'))
    parser.add_argument("file3")#, type=argparse.FileType('w'))
    return parser.parse_args()

args = parse_args()
u = md.Universe(args.file1, args.file2) #the trajectory could do .trr
computeDistCenterAxis(u, args.file3)

#import Calphascript
#import MDAnalysis as md
#u = md.Universe("all_c_long_pro.gro","all_c_long_pro_short.xtc")
#Calphascript.computeDistCenterAxis(u, "CA_dist.dat",1,10)
