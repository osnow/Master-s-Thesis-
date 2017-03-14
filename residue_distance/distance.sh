ref=$1
traj=$2
out=$3
type=$4
res1=$5
res2=$6

$VMD -dispdev text -e distance.tcl -args $ref $traj $out $type $res1 $res2