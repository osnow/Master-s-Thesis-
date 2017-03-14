
Run the script with

``./helix_twist.sh pdb traj output helix`` 

(0) pdb: name of the pdb file 
(1) traj: name of the trajectory file (format required .xtc)
(2) output: name of the output file
(3) helix: Residue selection in VMD format for transmembrane helix; resid_242_265 (i.e. transmembrane domain residues of GluCl) 

Output Format: Tab seperated file with 6 column: Frame (Time), average angle over 5 subunits, indivudual angles for each subunit.

Example: You can test the scripts with the sample trajectory and the pdb provided in the examples folder. To calculate the angle of the gating helix use this selection resid_242_265.

**KNOWN ISSUES**

- Trajectory and pdb files should be aligned so that the z component of the principal axes is parallel to the pore. 

- Fitting and periodic boundary should be handled before.
 
- Selections should be provided without any spaces, with underscores: i.e.: resid_211_to_339. Provide only the residue ids. The script selects the protein and the Calpha atoms by default. 