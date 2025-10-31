import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = 5 / (x**2 - 9)

plt.plot(x, y, 'b-', linewidth=2)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) = 5/(x² - 9)')
plt.show()
