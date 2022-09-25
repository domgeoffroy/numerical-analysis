import numpy as np
import matplotlib.pyplot as plt
 
# generating data
x = np.linspace(0, 10, 30)
y = np.sin(x)
 
plt.plot(x, y, c='blue', ls='--', lw=1, alpha=0.5)
plt.scatter(x, y, c='red', marker='+')
plt.show()
