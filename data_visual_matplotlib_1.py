import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

x = np.linspace(0,10,1000)

fig = plt.figure()
ax = plt.axes()

plt.plot(x, np.sin(x), 'k:', label='sin(x)')
plt.plot(x, np.cos(x), 'r--', label='cos(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('function sin(x)')
plt.legend()

plt.show()