mol load pdb [lindex $argv 0] xtc [lindex $argv 1]

set nf [molinfo top get numframes]

echo [lindex $argv 3]

source [lindex $argv 3]

start_sscache

for {set i 1} {$i < $nf } {incr i} {
    animate goto $i
}
file rename ss_traj.dat  [lindex $argv 2].dat
quit