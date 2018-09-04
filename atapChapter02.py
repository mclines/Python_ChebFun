import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

n = 16

tt = np.linspace(0,math.pi,n+1)

zz = np.exp(1j*tt)

plt.plot(zz,'.-k')

plt.savefig('figure01.png')

