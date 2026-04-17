import math
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.5)
y=x**2+3*x+2
plt.plot(x,y)
plt.title('Graphe de fonction')
plt.xlabel('abcisse')
plt.ylabel('ordonnée')
plt.grid(True)
plt.show()
tx,ty=[],[]
for i in np.arange(-5,5,0.01):
    y=math.sin(i)
    tx.append(i)
    ty.append(y)
plt.plot(tx,ty)
plt.title('Graphe de fonction sinus')
plt.xlabel('abcisse')
plt.ylabel('ordonnée')
plt.grid(True)
plt.show()
tx , ty=[],[]
for i in np.arange(-5,5,0.1):
    y=math.exp(-1*i)
    tx.append(i)
    ty.append(y)
plt.plot(tx,ty)
plt.title('Graphe de fonction exponentielle')
plt.xlabel('abcisse')
plt.ylabel('ordonnée')
plt.grid(True)
plt.show()