import math
import numpy as np

def chebpts(n):
  '''
chebpts(n) will return the Chebyshev points with respect to parameter n. This is achieved by computing the (2n)th roots of unity in the upper half of the complex plane and then creating an array of their real parts. 
  '''

  plane = np.linspace(0,math.pi,n) # Initalize an array of evenly spaced points in [-1,1]
  rootsOfUnity = np.exp(1j*plane) # Use the previous array to get the (2n)th roots of unity.
  points = np.real(rootsOfUnity) # Create an array of the chebyshev points from the (2n)th roots of unity. 
  return points
