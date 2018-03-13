import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.arange(11)
print x
mfx = fuzz.trimf(x,[0,3,5])

plt.plot(x,mfx)
plt.grid()
plt.show()
