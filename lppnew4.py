import matplotlib.pyplot as plt
import numpy as np
#Maximize z= x+5y
#subject to 5x+6y<=30
#           3x+2y<=12
fig, ax = plt.subplots()
x = np.linspace(0, 10, 400)
y = np.linspace(0, 10, 400)
X, Y = np.meshgrid(x, y)
plt.plot([6,0], [0,5], label=r'$5x+6y\leq30$')
plt.plot([4,0], [0,6], label=r'$3x+2y\leq12$')
plt.fill_between(x, 0, ((30-5*x)/6),where=((30-5*x)/6)>=0, interpolate=True, alpha=0.3, color='red')
plt.fill_between(x, 0,((12-3*x)/2) ,where=((12-3*x)/2)>=0, interpolate=True, alpha=0.3, color='blue')
plt.plot([5,0],[0,1],label='z=5')
plt.plot([10,0],[0,2],label='z=10')
plt.plot([20,0],[0,4],label='z=20')
plt.plot([25,0],[0,5],label='z=25')
plt.scatter(0,5,marker='o',color='red',label='optimal point',zorder=10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Maximize z= x+5y\nsubject to 5x+6y<=30\n3x+2y<=12')
plt.legend()
plt.grid(True)
plt.show()