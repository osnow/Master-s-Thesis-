#!/bin/bash

#plot domain twist
/opt/local/bin/python2.7 ~/Analysis/scripts/domain-twist/plot_domain_twist.py dtwist.dat

#plot helix twist
/opt/local/bin/python2.7 ~/Analysis/scripts/helix_twist/plot_helix_twist.py htwist.dat

#plot helix tilt
/opt/local/bin/python2.7 ~/Analysis/scripts/helix_tilt/plot_helix_tilt.py htilt.dat

