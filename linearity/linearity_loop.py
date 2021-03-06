#!/usr/bin/python

import numpy as np
import os
import time

lower = 0.5
upper = 10
Nsteps = 20

fileName = "linearity_V"
obsNames = "Dorra_Richter"

times = np.linspace(lower,upper,Nsteps)
for timex in times:
    os.system('ccdread -C 0 -b 2 -g 5 -F {fileName} -e {expTime} -o {fileName}{expTime} -u {obsNames} -C 1'.format(fileName=fileName, expTime=str(timex), obsNames=obsNames))
    print "Preparing for next image - don't interrupt now!"

