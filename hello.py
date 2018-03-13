#!usr/bin/python 2.7.12
import fuzzy
import numpy as np
import matplotlib.pyplot as chart
 
def main():
	a = []
	x = np.arange(0,4,0.01) 
	for i in range(len(x)):
		a.append(find_membership_gaussian(x[i], 2,1.184))
	chart.plot(x,a)
	chart.grid()
	chart.show()
	
if __name__ == '__main__':
	main()
