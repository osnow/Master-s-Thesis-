import os, re, argparse
parser = argparse.ArgumentParser(description='Saltbridge Data from VMD')
parser.add_argument('--inp', metavar='InPut', nargs=1, help='SB.dat file')
parser.add_argument('--sim_length', metavar='SimLength', nargs=1, help='simulation length')

args=parser.parse_args()

dat=open(args.inp[0],"r").readlines()
nr=int(args.sim_length[0])
out=open("count_"+args.inp[0],"w")

#sb_sum={}

bridge=False
summed=[]
pair=[]
for line in dat:
    if "freeSelLabel" in line:
        pair.append(line.split()[1].strip())
        bridge=False
    elif "freeSelString" in line or line.startswith("#"):
        bridge=False
    elif line.startswith('0'):
        bridge=True
    if bridge is True:
        summed.append(line.split()[1].strip())
#summed=[x for x in summed if x != "same"]
#    summed=[int(i) for i in summed]
#print len(summed)
chunks=[summed[x:x+nr] for x in xrange(0, len(summed), nr)]

for i in range(0, len(pair)):
    out.write(pair[i]+'\t'+str(sum(map(int,chunks[i])))+'\n')

out.close()
