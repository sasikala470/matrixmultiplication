import matplotlib.pyplot as plt
import numpy as np
Fs=5000
f=50
sample=1000
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.plot(x,y)
plt.xlabel("....>time")
plt.ylabel("....>amplitude")
plt.show()
