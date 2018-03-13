#!usr/bin/python 2.7.12
#Example from John Lilly's Fuzzy- 8.1
#Batch Least square Fuzzy Estimation For single input system
#best estimate not calculated here, Use matlab to calculate best estimate
#code just shows simulation
#Consider funct g(x) = x - cos(1.5x) + sin(0.4x)

import numpy as np
import matplotlib.pyplot as chart

centre = [0,2,4,6]
spread = 2.1784
e = 2.718	

def find_epsilon(x,j,parameter):
	sum_epsilon = 0
	epsilon = np.zeros((4,))
	epsilon_j = 0
	
	for i in range(4):
		epsilon[i] = e**(-0.5*(((x - centre[i]) / spread)**2))
		sum_epsilon += epsilon[i]
	
	if parameter == 0:
		return (epsilon[j]/sum_epsilon)
	
	else :
		return (epsilon[j])

def make_basis_function():	
	epsilon = [[],[],[],[]]
	x = 0 
	sum_x = [[],[],[],[]] 
	
	for i in range(4):	
		x = 0
		
		while x <6:
			epsilon[i].append(find_epsilon(x,i,0))
			sum_x[i].append(x)
			x += 0.05	
		
		chart.plot(sum_x[i],epsilon[i])
	
	chart.title('Basis Function made by Gaussian Membership')
	chart.grid()
	chart.show()
	return epsilon, sum_x[0]

def show_g():
	x = 0
	g = []
	sum_x =[]
	
	while x< 6:
		g.append(x - np.cos(1.5*x)+np.sin(0.4*x))
		sum_x.append(x)
		x += 0.05
	
	return g

def make_pair(epsilon, theta):
	paired = np.array(epsilon)
	total = []
	k = 0
	
	for i in range(len(paired[0])):	
		for j in range(4):
			k += theta[j]*paired[j][i]
		
		total.append(k)
		k = 0
	
	return total
	
def main():
	theta_old = [-2.660,5.4934,2.6386,8.7027]
	theta_less = [-1.0700, 3.86262, 4.0212, 7.5119]
	theta = [-18.0655, 28.8548, -18.9838, 21.6675]

	sampled_y =	[]
	psi = [ [],[],[],[],[],[],[] ]
	g = show_g()
	
	for i in range(7):
		sampled_y.append(i - np.cos(1.5*i)+np.sin(0.4*i))
		
		for j in range(4):
			psi[i].append(find_epsilon(i,j,0))
	
	epsilon, x = make_basis_function()
	total = make_pair(epsilon, theta)
	chart.plot(x,total)
	chart.plot(x,g,'r--')
	chart.title('Final Estimate to Given Function')
	chart.grid()
	chart.show()

if __name__ == '__main__' :
	main()

