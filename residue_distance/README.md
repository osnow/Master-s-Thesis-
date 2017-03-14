Run the script with 

``./distance.sh pdb traj output type residue1 residue2``

(0) pdb: name of the pdb file
(1) traj: name of the trajectory file (format required .xtc)
(2) output: name of the output file
(3) type: (intersubunit or intrasubunit)
(4) residue1: residue number
(5) residue2: residue number

Output Format: Tab seperated file with 6 column: Frame (Time), average distance over 5 subunits, indivudual measurements from each subunit.

**KNOWN ISSUES**

- Trajectory should be fixed for periodic boundary conditions. 

- Type intersubunit not written yet.
 
- By default script calculates the CA distances. 