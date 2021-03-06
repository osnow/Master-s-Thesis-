#!/bin/bash

#runs the plot average script for each angle type for each system - update when run new systems - also need to alter plot_average to have correct titles


python ../scripts/plot_average.py ../4NPQ_WT_ph46/dtwist.dat ../4NPQ_WT_pH70/dtwist.dat ../4NPQ_BA2_pH46/dtwist.dat ../4NPQ_I9T_pH46/dtwist.dat ../4HFI_WT_pH46/dtwist.dat ../4HFI_WT_pH70/dtwist.dat ../4NPQ_F238L_pH46/dtwist.dat ../4NPQ_I9T_pH46_2/dtwist.dat ../4NPQ_233_238_mut_pH46/dtwist.dat

python ../scripts/plot_average.py ../4NPQ_WT_ph46/htwist.dat ../4NPQ_WT_pH70/htwist.dat ../4NPQ_BA2_pH46/htwist.dat ../4NPQ_I9T_pH46/htwist.dat ../4HFI_WT_pH46/htwist.dat ../4HFI_WT_pH70/htwist.dat ../4NPQ_F238L_pH46/htwist.dat ../4NPQ_I9T_pH46_2/htwist.dat ../4NPQ_233_238_mut_pH46/htwist.dat

python ../scripts/plot_average.py ../4NPQ_WT_ph46/htilt.dat ../4NPQ_WT_pH70/htilt.dat ../4NPQ_BA2_pH46/htilt.dat ../4NPQ_I9T_pH46/htilt.dat ../4HFI_WT_pH46/htilt.dat ../4HFI_WT_pH70/htilt.dat ../4NPQ_F238L_pH46/htilt.dat ../4NPQ_I9T_pH46_2/htilt.dat ../4NPQ_233_238_mut_pH46/htilt.dat
