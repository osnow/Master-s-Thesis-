#!/bin/bash

EC=resid_5_to_195
TM=resid_196_to_315
hel_sel=resid_221_to_243
pdb=$1
xtc=$2

#calculate domain twist angles
bash ../scripts/domain-twist/twist.sh $pdb $xtc dtwist.dat $TM $EC 

#calculate helix tilt angles
bash ../scripts/helix_tilt/helix_tilt.sh $pdb $xtc htilt.dat $hel_sel

#calculat helix twist angles
bash ../scripts/helix_twist/helix_twist.sh $pdb $xtc htwist.dat $hel_sel

