ref=$1
traj=$2
out=$3
resnr=$4

$VMD -dispdev text -e traj_play_ss.tcl -args $ref $traj $out $ss_traj

. ./for_seq_log.sh $out $resnr