import matplotlib.pyplot as plt
import numpy as np
#Maximize z= 2x+5y
#subject to x+y<=8
#           x<=4
#           y<=6
fig, ax = plt.subplots()
x = np.linspace(0, 10, 400)
y = np.linspace(0, 10, 400)
X, Y = np.meshgrid(x, y)
plt.plot([8, 0],[0, 8], label=r'$x+y\leq8$')
plt.fill_between(x, 0, (8-x),where=(8-x)>=0, interpolate=True, alpha=0.3, color='red')
plt.axvline(x=4, color='black', linestyle='solid', linewidth=2, label=r'$x\leq4$')
plt.fill_betweenx(y, 0, 4, color='green', alpha=0.3, label=r'$x\leq2$')
plt.axhline(y=6, color='black', linestyle='solid', linewidth=2, label=r'$y\leq6$')
plt.fill_betweenx(x, 0, 17.5,where=(y<=6), color='green', alpha=0.3, label=r'$y\leq6$')
plt.plot([5,0],[0,2],label='z=10')
plt.plot([10,0],[0,4],label='z=20')
plt.plot([15,0],[0,6],label='z=30')
plt.plot([17,0],[0,6.8],label='z=34')
plt.scatter(2,6,marker='o',color='red',label='optimal point',zorder=10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Maximize z= 2x+5y\n subject to x+y<=8\n x<=4 \ny<=6')
plt.legend()
plt.grid(True)
plt.show()