import math
import numpy as np
import matplotlib.pyplot as plt
tx=[]
ty=[]
for i in np.arange(-5,5,0.5):
    y=i**2+3*i+2
    tx.append(i)
    ty.append(y)
plt.plot(tx,ty)
plt.title('Graphe de fonction')
plt.xlabel('abcisse')
plt.ylabel('ordonnée')
plt.grid(True)
plt.show()
tx,ty=[],[]
for i in np.arange(-5,5,0.5):
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
