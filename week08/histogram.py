#messing with histograms
#Author: Sarah Hastings

import numpy as np
import matplotlib.pyplot as plt #as plt can call whatever like
#get some random data

#np.random.seed(1) #number that comes out will be same each time, handy when debugging
normData = np.random.normal(size=10000)

plt.hist(normData)
plt.show()