#Shows a Visual of Gaussian Fuzzy membership functions
#Every Curve Defines a membership function
#The firing of a particular set at some X is given by the Y-coordinate of the of that Set at that particular X.
#include
import matplotlib.pyplot as chart
import numpy as np

def find_y(x, centre, spread):
		e = 2.71828
		y = e**(-0.5*(((x-centre)/spread)**2))
		return y
		
def main():
	i = 0
	y = [[],[],[],[],[],[]]
	x = []
	while i < 6:
		y[0].append(find_y(i, 1, 1.184))
		y[1].append(find_y(i, 2, 1.184))
		y[2].append(find_y(i, 3, 1.184))
		y[3].append(find_y(i, 4, 1.184))
		y[4].append(find_y(i, 5, 1.184))
		y[5].append(find_y(i, 6, 1.184))

		x.append(i)
		i = i+0.01
	
	chart.plot(x,y[0])
	chart.plot(x,y[1])
	chart.plot(x,y[2])
	chart.plot(x,y[3])
	chart.plot(x,y[4])
	chart.plot(x,y[5])

	chart.grid()
	chart.show()

if __name__ == '__main__' :
	main()

	
