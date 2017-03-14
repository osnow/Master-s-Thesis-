.. _analysis:

***********************
**Trajectory Analysis**
***********************
Different scripts I use to analyze the simulations of pentameric ligand-gated ion channels are provided here. In future updates these scripts will be applicable to any type of membrane protein.

In almost all the cases the calculation starts from a pdb and a corresponding trajectory file. To reduce the memory requirements and loading times please strip away anythin but the protein from the input files (Depending on the size of the trajectory vmd might crash unexpectedly). Also periodic boundary treatment of the trajectories and fitting to the z axis should be done before running any of the analysis tools. 

**Domain-Twist**
================
The script calculates the angle between two domains using the center of masses (COM). COM of each domain is projected onto the xy plane perpendecilar to the channel axis. With this convention the angle is defined between the vectors drawn from COM of the receptor to the COM of each domain.

.. image:: ../source/images/Domain-Twist.jpg
 
Requirements:
^^^^^^^^^^^^^
VMD

How to Use:
^^^^^^^^^^^
.. include:: ../analysis/domain-twist/README.md

**Helix Angles: Tilt & Twist**
==============================
This script calculates the tilt angle of the transmembrane helices relative to the channel axis in pentameric ligand-gated ion channels. In order to get comparable projections of helical axes, a reference structure is aligned to the center of mass of each M2 helix prior to the calculation (pdb file provided is taken as reference). X axis is defined between the center of mass of M2 helix and the center of mass of the receptor. Z axis is defined as the channel axis and finally Y axis taken as the vector normal to the XZ plane. With these axes definitions, the tilt angle is calculated between the projected helical axis onto XZ plane and Z axis and the twist angle between the projected helical axis onto YZ plane and Z axis. To summarize tilt angle represents the seperation of the M2 helices from the channel axis and the twist angle represents the radial movement.

.. image:: ../source/images/helix_tilt-twist.jpg

Requirements:
^^^^^^^^^^^^^
VMD, Orient and lapack packages for VMD

How to Use (Twist):
^^^^^^^^^^^^^^^^^^^
.. include:: ../analysis/helix_twist/README.md

How to Use (Tilt):
^^^^^^^^^^^^^^^^^^
.. include:: ../analysis/helix_twist/README.md

**Ca-Ca distance**
==================
Measuring Ca distance is a trivial task using any gromacs tools. However with pentameric symettry, it is possible that the minimum distance between two residues is not always the desired outcome. To overcome this, I had to create an index file with at least 10 entries and loop over it. Well, same calculation with VMD is more flexible and does not require an extra index file. Therefore I prefer to use VMD for distance analysis over GROMACS tools in some cases.

Requirements:
^^^^^^^^^^^^^
VMD

How to Use:
^^^^^^^^^^^
.. include:: ../analysis/residue_distance/README.md

**Salt Bridge Analysis**
========================
VMD Timeline Plugin provides a beatiful interface for salt bridge analysis over a trajectory. You can obtain the data matrix for plotting in the desired format. The scripts under this section takes salt bridge analysis data of two simulations, calculates the percantage value for each residue pair and outputs one joint file for bar plot representation. Usually the data is noisy, so you want to apply some sort of a filter in order to get catch only relevant changes. 

Requirements:
^^^^^^^^^^^^^
R, python 2.7

How to Use:
^^^^^^^^^^^
.. include:: ../analysis/salt_bridges/README.md

**Secondary Structure Sequence Logos**
======================================
The conventional way of representing the secondary structure data is to use 3D surface mapping. I have been searching for another way to represent the data since comparing these colored plots with each other did not feel quantitave. I came across a tutorial on MBG Clusters page which represented the secondary structure data in a similar fashion as DNA/RNA/Protein sequences. For an example see the supplementary material of `Yoluk et al. (2015) <http://pubs.acs.org/doi/abs/10.1021/acschemneuro.5b00111>`_.

Requirements:
^^^^^^^^^^^^^
`Weblogo <http://weblogo.berkeley.edu>`_ , `ss_traj.tcl <http://nefeli.mbg.duth.gr/cgi-bin/wiki.pl/Secondary_structure_analysis_of_protein_trajectories>`_ 

How to Use:
^^^^^^^^^^^
.. include:: ../analysis/ss_stride/README.md
