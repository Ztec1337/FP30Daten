#!/usr/bin/python

import numpy as np
import os
import time

lower = 0.5
upper = 10
Nsteps = 20
obsNames = "Dorra_Richter"

fileName1 = "sensitivity_I_1_"
fileName2 = "sensitivity_I_2_"
times = np.linspace(lower,upper,Nsteps)
for timex in times:
    os.system('ccdread -C 0 -b 2 -g 5 -F {fileName} -e {expTime} -o {fileName}{expTime} -u {obsNames} -C 1'.format(fileName=fileName1, expTime=str(timex), obsNames=obsNames))
    os.system('ccdread -C 0 -b 2 -g 5 -F {fileName} -e {expTime} -o {fileName}{expTime} -u {obsNames} -C 1'.format(fileName=fileName2, expTime=str(timex), obsNames=obsNames))
    print "Preparing for next pair of images - don't interrupt now!"

