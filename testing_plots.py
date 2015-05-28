'''the graph stuff'''

import numpy as np
import matplotlib as mpl
x_range = np.arange(0.1, 10., 0.01)
np.sin(np.pi/2)
import matplotlib.pyplot as plt
y_range = np.sin(x_range)
plt.plot(x_range, y_range, 'g')
plt.savefig('mysinegraph2')
