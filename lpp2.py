import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

c = [-4, -1]
A = [[1, 1],
     [3, 1]]
b = [50, 90]
x_bounds = (0, None)
y_bounds = (0, None)
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
optimal_x, optimal_y = result.x
fig, ax = plt.subplots()
x = np.linspace(0, 100, 400)
y = np.linspace(0, 100, 400)
X, Y = np.meshgrid(x, y)
plt.plot([50, 0],[0, 50], label=r'$x+y\leq50$')
plt.plot([30, 0],[0, 90], label=r'$3x+y\leq90$')
plt.fill_between(x, 0, (50-x),where=(50-x)>=0, interpolate=True, alpha=0.3, color='red')
plt.fill_between(x, 0,90-3*x ,where=(90-3*x)>=0, interpolate=True, alpha=0.3, color='blue')
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
