mol load pdb [lindex $argv 0]
mol load pdb [lindex $argv 0]
mol load pdb [lindex $argv 0]
mol load pdb [lindex $argv 0]
mol load pdb [lindex $argv 0]
mol load pdb [lindex $argv 0] xtc [lindex $argv 1]
set output_file [open [lindex $argv 2] w]
set vmdsel_helix [lindex $argv 3]
regsub -all {_} $vmdsel_helix " " vmdsel_helix

package require Orient
namespace import Orient::orient

proc angle_proj { tm_vec tm_center z_vec all_center } {
    set x_vec [vecnorm [vecsub $all_center $tm_center]]
    set z_vec [vecnorm $z_vec]
    set n_vec [vecnorm [veccross $x_vec $z_vec]]
    set dot [vecdot $tm_vec $n_vec]
    set tm_proj_xy [vecsub $tm_vec [vecscale $dot $n_vec]]
    set angle [angle $z_vec $tm_proj_xy]
    puts $angle
    return $angle
    }


proc angle { a b } {
    set amag [veclength $a]
    set bmag [veclength $b]
    set dotprod [vecdot $a $b]
    return [expr 57.2958 * acos($dotprod / ($amag * $bmag))]
}


set num_steps [molinfo top get numframes]
set TM2_A [atomselect 5 "chain A and $vmdsel_helix and name CA" frame 0]
set TM2_B [atomselect 5 "chain B and $vmdsel_helix and name CA" frame 0]
set TM2_C [atomselect 5 "chain C and $vmdsel_helix and name CA" frame 0]
set TM2_D [atomselect 5 "chain D and $vmdsel_helix and name CA" frame 0]
set TM2_E [atomselect 5 "chain E and $vmdsel_helix and name CA" frame 0]

set ALL_A [atomselect 0 "name CA"]
set move_A [atomselect 0 "all"]
set ALL_B [atomselect 1 "name CA"]
set move_B [atomselect 1 "all"]
set ALL_C [atomselect 2 "name CA"]
set move_C [atomselect 2 "all"]
set ALL_D [atomselect 3 "name CA"]
set move_D [atomselect 3 "all"]
set ALL_E [atomselect 4 "name CA"]
set move_E [atomselect 4 "all"]

set com_tm2a [measure center $TM2_A weight mass]
set com_alla [measure center $ALL_A weight mass]
set diff_a [vecsub $com_tm2a $com_alla]
$move_A moveby $diff_a
set I_all_A [draw principalaxes $ALL_A]

set com_tm2b [measure center $TM2_B weight mass]
set com_allb [measure center $ALL_B weight mass]
set diff_b [vecsub $com_tm2b $com_allb]
$move_B moveby $diff_b
set I_all_B [draw principalaxes $ALL_B]

set com_tm2c [measure center $TM2_C weight mass]
set com_allc [measure center $ALL_C weight mass]
set diff_c [vecsub $com_tm2c $com_allc]
$move_C moveby $diff_c
set I_all_C [draw principalaxes $ALL_C]

set com_tm2d [measure center $TM2_D weight mass]
set com_alld [measure center $ALL_D weight mass]
set diff_d [vecsub $com_tm2d $com_alld]
$move_D moveby $diff_d
set I_all_D [draw principalaxes $ALL_D]

set com_tm2e [measure center $TM2_E weight mass]
set com_alle [measure center $ALL_E weight mass]
set diff_e [vecsub $com_tm2e $com_alle]
$move_E moveby $diff_e
set I_all_E [draw principalaxes $ALL_E]

for {set frame 0} {$frame < $num_steps} {incr frame} {
    set TM2_A [atomselect 5 "chain A and $vmdsel_helix and name CA" frame $frame]
    set TM2_B [atomselect 5 "chain B and $vmdsel_helix and name CA" frame $frame]
    set TM2_C [atomselect 5 "chain C and $vmdsel_helix and name CA" frame $frame]
    set TM2_D [atomselect 5 "chain D and $vmdsel_helix and name CA" frame $frame]
    set TM2_E [atomselect 5 "chain E and $vmdsel_helix and name CA" frame $frame]
    
    set I_tm2a [draw principalaxes $TM2_A]
    set com_tm2a [measure center $TM2_A weight mass]
    set com_tm2a [lreplace $com_tm2a 2 2 [lindex $com_alla 2]]
    set angle_A [angle_proj [lindex $I_tm2a 2] $com_tm2a [lindex $I_all_A 2] $com_alla]

    set I_tm2b [draw principalaxes $TM2_B]
    set com_tm2b [measure center $TM2_B weight mass]
    set com_tm2b [lreplace $com_tm2b 2 2 [lindex $com_allb 2]]
    set angle_B [angle_proj [lindex $I_tm2b 2] $com_tm2b [lindex $I_all_B 2] $com_allb]

    set I_tm2c [draw principalaxes $TM2_C]
    set com_tm2c [measure center $TM2_C weight mass]
    set com_tm2c [lreplace $com_tm2c 2 2 [lindex $com_allc 2]]
    set angle_C [angle_proj [lindex $I_tm2c 2] $com_tm2c [lindex $I_all_C 2] $com_allc]

    set I_tm2d [draw principalaxes $TM2_D]
    set com_tm2d [measure center $TM2_D weight mass]
    set com_tm2d [lreplace $com_tm2d 2 2 [lindex $com_alld 2]]
    set angle_D [angle_proj [lindex $I_tm2d 2] $com_tm2d [lindex $I_all_D 2] $com_alld]

    set I_tm2e [draw principalaxes $TM2_E]
    set com_tm2e [measure center $TM2_E weight mass]
    set com_tm2e [lreplace $com_tm2e 2 2 [lindex $com_alle 2]]
    set angle_E [angle_proj [lindex $I_tm2e 2] $com_tm2e [lindex $I_all_E 2] $com_alle]
    
    set avg [expr ($angle_A+$angle_B+$angle_C+$angle_D+$angle_E)/5]
    
    puts $output_file "$frame $avg $angle_A $angle_B $angle_C $angle_D $angle_E"
}
close $output_file

quit
