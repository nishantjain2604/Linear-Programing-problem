import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

c = [-3, -9]
A = [[1, 3],
     [-1, -1],
     [1,-1]]
b = [60, -10, 0]
x_bounds = (0, None)
y_bounds = (0, None)
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
optimal_x, optimal_y = result.x
fig, ax = plt.subplots()
x = np.linspace(0, 60, 400)
y = np.linspace(0, 60, 400)
X, Y = np.meshgrid(x, y)
plt.plot([0, 60], [20, 0], label=r'$x+3y\leq60$')
plt.plot([0, 10], [10, 0], label=r'$x+y\geq10$')
plt.fill_between(x,0, ((60-x)/3) ,where=((60-x)/3)>=0, interpolate=True, alpha=0.3, color='red')
plt.fill_between(x, (10-x),20 ,where=(10-x)<=20, interpolate=True, alpha=0.3, color='blue')
plt.fill_between(x, y ,60 , interpolate=True, alpha=0.3, color='green')
plt.plot(x,x,label=r'x \leq y$')
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
