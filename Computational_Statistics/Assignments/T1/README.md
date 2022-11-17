# Assignment 1

The assignment has two objectives: (i) to derive the closed formula for the expected distance between two points sampled uniformly on a disk of radius R; and (ii) to simulate this same integral using the Metropolis-Hastings method and present diagnostics and performance measures. 

This repo is structured as follows:

- [X] t1.md: solution to the proposed exercises.
	- [X] Part I 
	- [X] Part II
	
- [.] Code
	- [.] MH_uniform_disc.py: contains proposal an acceptance probability. This script is used in notebook.py with the functions needed to run the Metropolis-Hastings method.
		- [X] Random Walk proposal
		- [ ] Local Optimization proposal: acceptance is not full implemented yet.
	- [.] notebook.py: contains the code for the simulation. Although is a python script, this file is intended to be run as jupyter notebook, allocating chunks of the code in proper cells.
		- [X] simulation for each radius R.
		- [ ] diagnostics.
		- [ ] performance measures: not implemented the way it should be. Need further work.
		- [ ] graphical representation of the results.
