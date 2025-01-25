#import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

data=genfromtxt("file.txt")
tempo=data[:,0]
ampiezza=data[:,1]
time=[]
amplitude=[]
# FARE ANCHE IL PLOT DELLA fft

for i in range (len(data)):
    time.append(tempo[i])
    amplitude.append(ampiezza[i])

time.pop(0)
amplitude.pop(0)
plt.plot(time,amplitude)
plt.show()

