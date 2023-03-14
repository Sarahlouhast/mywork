#messing with piechart
#Author: Sarah Hastings

import numpy as np
import matplotlib.pyplot as plt #as plt can call whatever like

fruit = np.array(['Apples', 'Orange', 'Bannana'])
numbers= np.array([23,77,500])

plt.pie(numbers, labels=fruit)
plt.legend()
plt.show()