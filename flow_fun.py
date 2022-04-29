import matplotlib.pyplot as plt
import numpy as np

def findC(b):
	c = 2*b+3
	return c

def calK(theta,Ks=6.95/100000,phi=0.4,b=5.39):
	if theta>phi:
		return Ks
	else:
		c = findC(b)
		K = Ks*(theta/phi)**c
		return K

def calPsi(theta,psiac=-47.8,phi=0.4,b=5.39):
	if theta <= phi:
		Psi = psiac*(phi/theta)**b
	else: 
		Psi = 0
	return Psi

def alpha(theta,phi=0.4):
	return 0.001*(theta*2+(1-phi)*1)
