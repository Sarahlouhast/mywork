#messing with matplotlin
#Author: Sarah Hastings

import numpy as np
import matplotlib.pyplot as plt #as plt can call whatever like

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label="xsquared")
plt.plot(xpoints, xpoints, label="straight", color="blue")
plt.legend()
plt.show() #to start up plot programe

#plt.savefig('lecture1') #to save
