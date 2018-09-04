import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import chebyshevFunctions as cf

# Any interval [a,b] can be scaled to [-1,1] so we will focus on [-1,1]. 

# n is just a positive integer, here it is chosen to be the same value as given in the text. 
n = 16

# tt is a numpy array of n+1 equally spaced points between 0 and pi, including 0 and pi.
tt = np.linspace(0,math.pi,n+1)

# zz is an array of the (2n)th roots of unity in the upper half of the complex plane.
zz = np.exp(1j*tt)

# Here we will initialize our figure and subplots for matplotlib.
fig,a = plt.subplots()

# This will build our desired plot as shown in figure01 on page 7 of the text.
a.scatter(np.real(zz),np.imag(zz))
a.plot(np.real(zz),np.imag(zz))
# This will save our plot to figure01.png
plt.savefig('figures/ch02/figure01.png')

# The chebyshev points with respect to parameter n are just the real parts of the (2n)th roots of unity in the upper half of the complex plane. Note that including the (2n)th roots of unity in the lower half of the complex plane would just repeat the same list of numbers since they would share the same real parts. 


XX = cf.chebpts(n)
r = np.array([0]*len(XX))
a.scatter(XX,r)
a.plot(XX,r)

plt.savefig('figures/ch02/figure02.png')


def f(x):
  '''
A simple step function for use in examples throughout the rest of chapter 02. 
  '''
  result = np.sign(x) - (1/2)*x
  return result

fig,b = plt.subplots()
grid = np.linspace(-1,1,50)

b.plot(grid,f(grid)) 

plt.savefig('figures/ch02/figure03.png')
