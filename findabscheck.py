import re
import sys
import glob
import numpy as np

transitionCheck = sys.argv[1]

w, f, e = np.loadtxt(transitionCheck, unpack=True)
midpoint = str(np.average(w))

print transitionCheck, midpoint[:6]

for file in glob.iglob('*/*.sig.dat'):
  for line in open(file, 'r'):
    valid = re.compile(r"^" + midpoint[:6])
    # if re.search(midpoint[:6], line.split()[0]):
    if re.search(valid, line.split()[0]):
      print file, line,

