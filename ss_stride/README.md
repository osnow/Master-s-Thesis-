Before running the script set the variables for $weblogo and $ss_traj . 

``weblogo=/path/to/weblogo``

``ss_traj=/path/to/ss_traj.tcl`` 

Run the script with 

``. ./run_stride_seqLogo.sh pdb traj output_name resnr``

Thhe initial dat is necessary because the suggested way to set variable above will not allow the run_stride_seqLogo.sh to access them.

Output format: Output is a pdf file. Length of the file is set by the sequence length. 

Example: within the ss_stride folder run

``. ./run_stride_seqlogo.sh ../../examples/GluCl.pdb ../../examples/GluCl_md4.xtc test 339``

The output you will get is similar to what I presented in the article Yoluk et al. (2015). In the article I have displayed only a short region. But the output you will get test_seqLogo.pdf contains the full sequence. When you open the file you will spot the individual beta strands and transmembrane helices right away. 