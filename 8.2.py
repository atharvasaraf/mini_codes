#! /usr/bin/python2.7.12
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(x) * (np.cos(y)**2)
def plot_func():
    fig = plt.figure()
    X = np.linspace(-1, 1, 10)
    Y = np.linspace(-1, 1, 10)
    X, Y = np.meshgrid(X, Y)
    Z = f(X,Y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()

def gauss_value(x, centre, spread):
    return e**(-0.5 * ( ((x-centre)/spread)**2 ) )

def 
if __name__ == '__main__':
    plot_func()
