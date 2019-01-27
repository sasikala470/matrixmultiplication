import matplotlib.pyplot as plt
import numpy as np
f1=5
Fs=50
A=5
sample=1000
x=np.arange(sample)
y=A*np.sin((2*np.pi*f1*x/Fs)+90)
plt.subplot(311)
plt.plot(x,y)

A1=10
y1=A1*np.sin((2*np.pi*f1*x/Fs)+90)
plt.subplot(312)
plt.plot(x,y1)  

z=y+y1
plt.subplot(313)
plt.plot(z)
plt.show()


