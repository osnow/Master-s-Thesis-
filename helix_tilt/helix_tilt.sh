ref=$1
traj=$2
out=$3
sel=$4
/Applications/VMD1.9.3.app/Contents/MacOS/startup.command -dispdev text -e ~/Analysis/scripts/helix_tilt/helix_tilt.tcl -args $ref $traj $out $sel
