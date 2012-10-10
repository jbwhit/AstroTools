About
=====

I've written a bunch of scripts that I felt were useful at one time. I'm keeping them in a github repo so that I can update and change them in a sensible way (and share them if anyone finds any use for them). 




MegaMind
========

This program is a meta-wrapper around several other programs. It's purpose is to make complicated and tedious Voigt profile fitting easier and more systematic. It does this by interfacing with both the supercomputer (green) and the program pyfit (which is a wrapper around the vpfit program).

If this seems like an needlessly complicated onion-layers of wrapping, you're probably right. Here's what the programs do starting at the most basic level. 


VPFIT
=====

The standard way we use vpfit is to send a string of commands to vpfit via the commandline. This string of commands specifies several things: 
 - chi-square stopping criteria
 - parameter step-sizes
 - input file (a *.13 format)
 - atomic data file
 - setup file (various details specified)

VPFIT then outputs two files: fort.18 (log of the fitting process) and fort.26 (final results with errors).

PYFIT
=====

Is a python wrapper that organises the process of using VPFIT. There are many different fit parameter strings that can be used. 

What it does:
 - creates a self-contained time-stamped directory for the whole process
 - creates symbolic links to the data files, atomic data files, etc. 
 - optionally restarts the fit if it stops after 125 iterations (default vpfit behaviour).
 - if the fit converges, optionally starts the fit allowing alpha to vary.
 - uses fort18analysis to analyse the fit (calculates AICc and various other things).
 - fitType (normalFit, alphaFit, velocityFit)
 - reports the results to a Google Spreadsheet
 
Back to MegaMind and what it will do. At the end of a pyfit run, the final analysis done will report a number of things: 
 - worst N errors
 - worst b errors
 - worst z errors
 - smallest/largest b values
 - worst region (est. by chi square/Npix)
 - mis-matched components (components that exist in MgII but not FeII)
 - components that are too close together

From 1 seed model
 - run a group of changes
 - automatically choose best by AIC which one is best (possibly re-run new tests on the best Nbest AICc results).


Running a command like: 
MegaMind fort13s/starting.0015.test.24.13 --layers 2 --ncomponents 5 --ncombinations 3 --test errors|bigsmallB --maxRuns 1 --level L5 --comment "megamind: " --fitType normalFitAlphaFit --bump
 - remove top N; N|(N-1) components selected by breakdown criteria
 - Halve b-value; halve b-value [and fix, and add narrow components to either size]; re-float b-value

What I expect to see should be a fort13s/megamind.23.13 fort13s/megamind.23.test.23.13 and it will create qsub script that is submitted to green. 


