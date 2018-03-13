#!/usr/bin/python 2.7.12

# Attempt to make a simple fuzzy controller
# Interpolator between Memoryless Function

#System Rules as given:
	# if x1 is p11 && x2 is p12 q1 = 1 + x1 + x2
	# if x1 is p11 && x2 is p22 q2 = 2x1 + x2
	# if x1 is p12 && x2 is p12 q3 = -1 + x1 - 2x2
	# if x1 is p12 && x2 is p22 q4 = -2 - x1 + 0.5x2

#Membership Functions as given(Gaussian):
	#u11 centre: -1 spread: 0.8493
	#u12 centre:  1 spread: 0.8493
	
	#u21 centre: -1 spread: 0.8493
	#u22 centre:  1 spread: 0.8493

# T-Norm is Product
# Result shows Output similar to sinusoid
import numpy as np
import matplotlib.pyplot as chart

eta = np.zeros((2,2)) 
spread = 0.8493
mu = np.zeros((4, ))
q = np.zeros((4,))
basic_val = np.zeros((4,))

	
def cal_membership(x, centre, spread):
	e = 2.7821
	val = e**(-0.5*(( (x - centre) / spread )**2))
	return val	

def rule_set(i,x1,x2):
	q[0] =  1+ x1 + x2
	q[1] =  2*x1 + x2
	q[2] = -1 + x1 - 2*x2
	q[3] = -2 - x1 + 0.5*x2
	return q[i]

def generate_membership(x1,x2):
	for i in range(2):
		if i==1:
			x = x2
		else:
			x = x1
		
		for j in range(2):
			if j==1:
				centre = 1
			else :
				centre = -1
		
			eta[i][j] = cal_membership(x, centre, spread)

def calculate_mu():
	for i in range (2):
		for j in range(2):
			mu[2*i + j] = eta[0][i] * eta[1][j]
	u = mu/np.sum(mu)	
	return u

def get_crisp(x1,x2):	
	crisp = 0
	for i in range(4):	
		crisp += mu[i]*rule_set(i,x1,x2)
	return crisp

def main():	
	output = []
	i =0
	
	while i < 2:
		x1 = -2+ i
		x2 = -1+ i
		generate_membership(x1,x2)	
		mu = calculate_mu()
		y_crisp = get_crisp(x1,x2)
		output.append(y_crisp)
		i = i + 0.01	
	
	chart.plot(output)
	chart.grid()
	chart.show()

if __name__ == '__main__':
	main()
