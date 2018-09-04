import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Any interval [a,b] can be scaled to [-1,1] so we will focus on [-1,1]. 

# n is just a positive integer, here it is chosen to be the same value as given in the text. 
n = 16

# tt is a numpy array of n+1 equally spaced points between 0 and pi, including 0 and pi.
tt = np.linspace(0,math.pi,n+1)

# zz is an array of the (2n)th roots of unity in the upper half of the complex plane.
zz = np.exp(1j*tt)

# Here we will initialize our figure and subplots for matplotlib.
fig,k = plt.subplots()

# This will build our desired plot as shown in figure01 on page 7 of the text.
k.plot(np.real(zz),np.imag(zz))

# This will save our plot to figure01.png
plt.savefig('figure01.png')

