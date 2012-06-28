#!/usr/bin/env python
import sys
import string
import numpy as np
import pylab as pl

filestring = []

shiftFile = sys.argv[1]
# shiftFile = 'vshift.w.w.w'

with open(shiftFile, 'rb') as fb:
  for line in fb:
    filestring.append(line)
    

# Taken from MM_VPFIT_2012-06-05_noiso.dat
qvalues = {}
qvalues['FeII2600'] =  {}
qvalues['FeII2586'] =  {}
qvalues['FeII2382'] =  {}
qvalues['FeII2374'] =  {}
qvalues['FeII2367'] =  {}
qvalues['FeII2344'] =  {}
qvalues['FeII2260'] =  {}
qvalues['FeII2249'] =  {}
qvalues['FeII1611'] =  {}
qvalues['FeII1608'] =  {}
qvalues['AlII1670'] =  {}
qvalues['AlIII1862'] = {} 
qvalues['AlIII1862'] = {} 
qvalues['AlIII1854'] = {} 
qvalues['AlIII1854'] = {} 
qvalues['SiII1526']  = {}
qvalues['MgI2852']   = {}
qvalues['MgI2026']   = {}
qvalues['MgII2796']  = {}
qvalues['MgII2803']  = {}

qvalues['FeII2600']['q'] =  1370.0 
qvalues['FeII2586']['q'] =  1515.0 
qvalues['FeII2382']['q'] =  1505.0 
qvalues['FeII2374']['q'] =  1625.0 
qvalues['FeII2367']['q'] =  1803.0 
qvalues['FeII2344']['q'] =  1375.0 
qvalues['FeII2260']['q'] =  1435.0 
qvalues['FeII2249']['q'] =  1604.0 
qvalues['FeII1611']['q'] =  1330.0 
qvalues['FeII1608']['q'] = -1165.0 
qvalues['AlII1670']['q'] =   270.0 
qvalues['AlIII1862']['q'] =    224.0 
qvalues['AlIII1862']['q'] =    224.0 
qvalues['AlIII1854']['q'] =    458.0 
qvalues['AlIII1854']['q'] =    458.0 
qvalues['SiII1526']['q']  =  47.0
qvalues['MgI2852']['q']   = 90.0
qvalues['MgI2026']['q']   = 87.0
qvalues['MgII2796']['q']  = 212.0
qvalues['MgII2803']['q']  = 121.0

with open(shiftFile + '.ascii', 'w') as outFile:
  for line in filestring:
    vshift = line.split()[3]
    verr = line.split()[4]
    if line.split()[-2] == '!':
      transition = line.split()[-1]
    else:
      transition = ''.join([line.split()[-2], line.split()[-1]])
    try:
      qvalues[transition]['vshift'] = float(vshift) * 1000.
      qvalues[transition]['verr'] = float(verr) * 1000.
      print >>outFile, float(vshift) * 1000., float(verr) * 1000.,
      print >>outFile, transition
    except:
      try:
        if float(verr) > 0.:
          qvalues[transition]['vshift'] = float(vshift[:-1]) * 1000.
          qvalues[transition]['verr'] = float(verr) * 1000.
          print >>outFile, float(vshift[:-1]) * 1000., float(verr) * 1000.,
          print >>outFile, transition
      except:
        try:
          if float(verr) > 0.:
            qvalues[transition]['vshift'] = float(vshift[:-2]) * 1000.
            qvalues[transition]['verr'] = float(verr) * 1000.
            print >>outFile, float(vshift[:-2]) * 1000., float(verr) * 1000.,
            print >>outFile, transition
        except:
          print "Not what you think it is...", transition

thingy = []
err = []
def weightedAverage(values, errors):
  """given two arrays values, and errors, compute weighted average."""
  weights = 1. / errors**2.
  return np.sum(weights * values) / np.sum(weights)
  
def weightedError(errors):
  """docstring for fname"""
  weights = 1. / errors**2.
  return 1. / np.sum(weights)

for tran in qvalues:
  if 'verr' in qvalues[tran]:
    pl.errorbar(qvalues[tran]['q'], qvalues[tran]['vshift'], yerr=qvalues[tran]['verr'])
    pl.scatter(qvalues[tran]['q'], qvalues[tran]['vshift'])
    thingy.append(qvalues[tran]['vshift'])
    err.append(qvalues[tran]['verr'])
pl.title(shiftFile)
pl.savefig(shiftFile + ".pdf")
# print np.average(thingy)
# weightedAverage(np.array(thingy), np.array(err))
# weightedError(np.array(err))
