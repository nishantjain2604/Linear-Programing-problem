import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

c = [200, 500]
A = [[-1, -2],
     [3, 4]]
b = [-10, 24]
x_bounds = (0, None)
y_bounds = (0, None)
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
optimal_x, optimal_y = result.x
fig, ax = plt.subplots()
x = np.linspace(0, 10, 400)
y = np.linspace(0, 10, 400)
X, Y = np.meshgrid(x, y)
plt.plot([10,0], [0,5], label=r'$x+2y\geq10$')
plt.plot([8,0], [0,6], label=r'$3x+4y\leq24$')
plt.fill_between(x, ((10-x)/2),10 ,where=((10-x)/2)<=10, interpolate=True, alpha=0.3, color='red')
plt.fill_between(x, 0,(24-3*x)/4 ,where=((24-3*x)/4)>=0, interpolate=True, alpha=0.3, color='blue')
ax.plot(optimal_x, optimal_y, 'ro', label='Optimal Point')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Linear Programming with Visualization')
plt.legend()
plt.grid(True)
plt.show()
print(f'Optimal x: {optimal_x:.2f}')
print(f'Optimal y: {optimal_y:.2f}')
print(f'Optimal Objective Value: {result.fun:.2f}')
