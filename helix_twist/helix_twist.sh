#!/bin/bash

ref=$1
traj=$2
out=$3
sel=$4
/Applications/VMD1.9.3.app/Contents/MacOS/startup.command -dispdev text -e ~/Analysis/scripts/helix_twist/helix_twist.tcl -args $ref $traj $out $sel
