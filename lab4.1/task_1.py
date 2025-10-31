import numpy as np
import matplotlib.pyplot as plt

x_degrees = np.linspace(-360, 360, 500)
x_radians = x_degrees * np.pi / 180

f_x = np.exp(np.cos(x_radians)) + np.log(np.cos(0.6*x_radians)**2 + 1) * np.sin(x_radians)
h_x = -np.log((np.cos(x_radians) + np.sin(x_radians))**2 + 2.5) + 10

plt.plot(x_degrees, f_x, 'b-')
plt.plot(x_degrees, h_x, 'r-')

plt.xlabel('Градусы')
plt.ylabel('y')
plt.show()