#!/usr/bin/python 2.7.12
# Attempt to simulate distributed Control with T-S fuzzy
#Rule Set:
#	xi_dot = ai*x(t) + bi*u(t)
#   a1 = [[0,1],[-2,2]]
#   a2 = [[0,1],[-3,2]]
#   a3 = [[0,1],[-2,1]]
#   a4 = [[0,1],[-3,1]]
#	bi = [0,1]
import numpy as np
import matplotlib.pyplot as chart
from scipy.integrate import ode

x1 = 0
x2 = 0
X = [0,0]
eta = np.zeros((2,2)) 
spread = 0.8493
mu = np.zeros((4, ))
q = np.zeros((4,))
basic_val = np.zeros((4,))
eta_norm = np.zeros((4,))

a1 = np.array(([0,1],[-2,2]))
a2 = np.array(([0,1],[-3,2])) 
a3 = np.array(([0,1],[-2,1]))
a4 = np.array(([0,1],[-3,1]))

bi= np.array([0,1])

k1 = [0, 4]
k2 = [-1,4]
k3 = [0, 3]
k4 = [-1,3]

def cal_membership(x, centre, spread):
	e = 2.7821
	val = e**(-0.5*(( (x - centre) / spread )**2))
	return val	

def generate_membership(X):
	for i in range(2):
		if i==1:
			x = X[1]
		else:
			x = X[0]
		
		for j in range(2):
			if j==1:
				centre = 1
			else :
				centre = -1
		
			eta[i][j] = cal_membership(x, centre, spread)
	
	for i in range(2):
		for j in range(2):
			eta_norm[2*i+j] = eta[0][i] * eta[1][j]
		
	return (eta_norm / np.sum(eta_norm)) 

def model(t, X):
	x1, x2 =X
		
	x1dot = 
	x2dot = 
	return [x1dot,x2dot]
	
def main():
	data_y = []	
	t = []
	
	solver = ode(model).set_integrator('vode',method='adams').set_initial_value(X0,t0)

	while solver.successful() and solver.t < t1:
		solver.integrate(solver.t+dt)
		data_y.append(solver.y)
		eta_norm = generate_membership(solver.y)
		t.append(solver.t)
	
	chart.plot(t,data_y)
	chart.grid()
	chart.show()
	print eta_norm
if __name__ == "__main__":
	main()
