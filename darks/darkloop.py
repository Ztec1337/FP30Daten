#!/usr/bin/python

import os
import time

for _ in range(200):
  os.system('ccdread -E 20 -F dark_ -o dark')
  os.system('ccdread -E 0 -F bias_ -o bias')
  print "Waiting 30s -- abort now with Ctrl-C if you want."
  time.sleep(20)
  print "Preparing for next image - don't interrupt now!"
  time.sleep(2)
