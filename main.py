import numpy as np
import matplotlib.pyplot as plt
y = np.arange(-150, 150.01, 0.01)


def func(x):
    function = -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
    return function

plt.title(f'Корней бесконечное множество')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.plot(y, func(y), 'g')
plt.legend()
plt.show()