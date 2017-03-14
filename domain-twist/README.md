
Run the script with your input parameters.

``./twist.sh pdb traj output domain1 domain2``

(0) pdb: name of the pdb file 
(1) traj: name of the trajectory file (format required multi pdb (can be easily modified to read other traj files))
(2) output: name of the output file
(3) domain1: Residue selection in VMD format for domain 1 prodived with underscores instead of spaces; resid_211_339 (i.e. transmembrane domain residues of GluCl) 
(4) domain2: Residue selection for domain 2. Same syntax as domain 1 applies; resid_1_210 (i.e. Extracellular domain of GluCl )

Output Format: Tab seperated file with 6 column: Frame (Time), average angle over 5 subunits, indivudual angles for each chain.

Example:
Within the directory where twist.sh script is located run

``bash twist.sh /path/to/stb_proteinart/examples/GluCl.pdb /path/to/stb_proteinart/examples/GluCl_md4.xtc twist.dat resid_211_to_339 resid_1_to_210``

The output you will get contains a reduced version of the data presented in artcile `Yoluk et al.(2015) <http://pubs.acs.org/doi/abs/10.1021/acschemneuro.5b00111>`_.

**KNOWN ISSUES**

- Trajectory and pdb files should be aligned so that the z component of the principal axes is parallel to the pore. 

- Fitting and periodic boundary should be handled before.
 
- Selections should be provided without any spaces, with underscores: i.e.: resid_211_to_339. Provide only the residue ids. The script selects the protein and the Calpha atoms by default. 