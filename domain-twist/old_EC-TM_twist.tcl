mol load pdb [lindex $argv 0] #xtc [lindex $argv 1]
#mol load pdb [lindex $argv 1] 
mol load xtc [lindex $argv 1]

set num_steps [molinfo 1 get numframes]

set ALL [atomselect 0 "name CA"]
set COM_all [measure center $ALL weight mass]
set output_file [open [lindex $argv 2] w]
set vmdsel_TM [lindex $argv 3]
set vmdsel_EC [lindex $argv 4]
regsub -all {_} $vmdsel_TM " " vmdsel_TM
regsub -all {_} $vmdsel_EC " " vmdsel_EC

for {set frame 0} {$frame < $num_steps} {incr frame} {
    foreach ch {A B C D E} {

	set TM [atomselect 1 "chain $ch and $vmdsel_TM and name CA" frame $frame]
	set EC [atomselect 1 "chain $ch and $vmdsel_EC and name CA" frame $frame]

	set COM_ec [measure center $EC weight mass]
	set COM_tm [measure center $TM weight mass]
	set COM_tm [lreplace $COM_tm 2 2 [lindex $COM_all 2]]
	set COM_ec [lreplace $COM_ec 2 2 [lindex $COM_all 2]]

	set vec1 [vecsub $COM_ec $COM_all]
	set vec2 [vecsub $COM_tm $COM_all]
	set dotprod [vecdot $vec1 $vec2]
	set angle_$ch [ expr 57.2958 * acos($dotprod / ([veclength $vec1] * [veclength $vec2]))]
    }

    set avg [expr ($angle_A+ $angle_B + $angle_C + $angle_D + $angle_E)/ 5]

    puts $output_file "$frame $avg $angle_A $angle_B $angle_C $angle_D $angle_E"
}

close $output_file

quit
