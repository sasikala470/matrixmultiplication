import matplotlib.pyplot as plt
import numpy as np
Fs=5000
f=5
sample=20000
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.subplot(311)
plt.plot(x,y)

Fs1=8000
f1=6
y1=np.sin(2*np.pi*f1*x/Fs1)
plt.subplot(312)
plt.plot(x,y1)

z=y+y1
plt.subplot(313)
plt.plot(z)
plt.show()
 

