import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

c = [-2, -1]
A = [[1, 1],
     [1, 2],
     [1, 0]]
b = [3, 5, 2]
x_bounds = (0, None)
y_bounds = (0, None)
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
optimal_x, optimal_y = result.x
fig, ax = plt.subplots()
x = np.linspace(0, 5, 400)
y = np.linspace(0, 5, 400)
X, Y = np.meshgrid(x, y)
plt.plot( [3, 0],[0, 3], label=r'$x+y\leq3$')
plt.plot( [2.5, 0],[0, 5], label=r'$x+2y\leq5$')
plt.axvline(x=2, color='black', linestyle='solid', linewidth=2, label=r'$x\leq2$')
plt.fill_between(x, 0, (5-x)/2.0,where=((5-x)/2.0)>=0, interpolate=True, alpha=0.3, color='red')
plt.fill_between(x, 0,3-x ,where=(3-x)>=0, interpolate=True, alpha=0.3, color='blue')
plt.fill_betweenx(y, 0, 2, color='green', alpha=0.3, label=r'$x\leq2$')
ax.plot(optimal_x, optimal_y, 'ro', label='Optimal Point')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Linear Programming with Visualization')
plt.legend()
plt.grid(True)
plt.show()
print(f'Optimal x: {optimal_x:.2f}')
print(f'Optimal y: {optimal_y:.2f}')
print(f'Optimal Objective Value: {-result.fun:.2f}')
